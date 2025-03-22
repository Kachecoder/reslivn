from typing import Any

from fastapi.responses import StreamingResponse as FastAPIStreamingResponse
from loguru import logger

from reworkd_platform.web.api.agent.stream_mock import stream_string
from reworkd_platform.web.api.agent.tools.reason import Reason
from reworkd_platform.web.api.agent.tools.tool import Tool
from reworkd_platform.schemas.user import UserBase
from reworkd_platform.db.crud.oauth import OAuthCrud

class ContentGeneration(Tool):
    description = (
        "Generate SEO-optimized marketing content for websites, landing pages, "
        "social media, and email campaigns.\n"
    )
    public_description = "Create marketing content optimized for SEO and conversions."
    arg_description = "The content type (website, landing page, social media, email), topic, target audience, and key points to include."
    image_url = "/tools/content.png"

    async def call(
        self, goal: str, task: str, input_str: str, user: UserBase, oauth_crud: OAuthCrud, *args: Any, **kwargs: Any
    ) -> FastAPIStreamingResponse:
        try:
            # Parse the input to extract content parameters
            content_params = self._parse_content_parameters(input_str)
            
            # Generate the appropriate content based on the content type
            if content_params["type"].lower() in ["website", "landing page", "web", "webpage"]:
                return await self._generate_web_content(goal, task, content_params)
            elif content_params["type"].lower() in ["social", "social media", "social post"]:
                return await self._generate_social_content(goal, task, content_params)
            elif content_params["type"].lower() in ["email", "newsletter"]:
                return await self._generate_email_content(goal, task, content_params)
            else:
                # Default to general marketing content
                return await self._generate_general_content(goal, task, content_params)
            
        except Exception as e:
            logger.exception(f"Error in content generation: {str(e)}")
            return await Reason(self.model, self.language).call(
                goal, task, input_str, user, oauth_crud, *args, **kwargs
            )

    def _parse_content_parameters(self, input_str: str) -> dict:
        """Parse the input string to extract content parameters"""
        # Default parameters
        params = {
            "type": "general",
            "topic": "",
            "audience": "general",
            "key_points": [],
            "tone": "professional",
            "length": "medium"
        }
        
        # Try to extract content type
        content_types = ["website", "landing page", "web", "webpage", "social", "social media", 
                        "social post", "email", "newsletter", "general"]
        for content_type in content_types:
            if content_type in input_str.lower():
                params["type"] = content_type
                break
        
        # Extract topic (assume it's the main subject after removing the content type)
        remaining_text = input_str.lower()
        for content_type in content_types:
            remaining_text = remaining_text.replace(content_type, "")
        
        params["topic"] = remaining_text.strip()
        
        # Look for audience indicators
        audience_indicators = ["for", "targeting", "audience", "demographic"]
        for indicator in audience_indicators:
            if indicator in remaining_text:
                parts = remaining_text.split(indicator, 1)
                if len(parts) > 1:
                    params["audience"] = parts[1].strip()
                    params["topic"] = parts[0].strip()
        
        return params

    async def _generate_web_content(self, goal: str, task: str, params: dict) -> FastAPIStreamingResponse:
        """Generate content for websites or landing pages"""
        prompt = f"""
        Create SEO-optimized content for a {params['type']} about {params['topic']} targeting {params['audience']}.
        
        The content should:
        1. Include an attention-grabbing headline
        2. Have a compelling introduction that addresses the audience's pain points
        3. Include key benefits and features
        4. Incorporate relevant keywords naturally for SEO
        5. Include a strong call-to-action
        6. Be formatted with appropriate HTML structure
        
        Goal: {goal}
        Task: {task}
        """
        
        return await self._generate_content_with_model(prompt)

    async def _generate_social_content(self, goal: str, task: str, params: dict) -> FastAPIStreamingResponse:
        """Generate content for social media posts"""
        prompt = f"""
        Create engaging social media content about {params['topic']} targeting {params['audience']}.
        
        The content should:
        1. Be attention-grabbing and shareable
        2. Include relevant hashtags
        3. Be concise and impactful
        4. Include a clear call-to-action
        5. Be optimized for engagement (likes, shares, comments)
        
        Goal: {goal}
        Task: {task}
        """
        
        return await self._generate_content_with_model(prompt)

    async def _generate_email_content(self, goal: str, task: str, params: dict) -> FastAPIStreamingResponse:
        """Generate content for email campaigns"""
        prompt = f"""
        Create compelling email marketing content about {params['topic']} targeting {params['audience']}.
        
        The content should:
        1. Have an attention-grabbing subject line
        2. Include a personalized greeting
        3. Have a clear and concise message
        4. Include a strong call-to-action
        5. Be formatted appropriately for email
        
        Goal: {goal}
        Task: {task}
        """
        
        return await self._generate_content_with_model(prompt)

    async def _generate_general_content(self, goal: str, task: str, params: dict) -> FastAPIStreamingResponse:
        """Generate general marketing content"""
        prompt = f"""
        Create marketing content about {params['topic']} targeting {params['audience']}.
        
        The content should:
        1. Be engaging and persuasive
        2. Highlight key benefits and features
        3. Address the audience's needs and pain points
        4. Include a clear call-to-action
        5. Be optimized for the intended marketing channel
        
        Goal: {goal}
        Task: {task}
        """
        
        return await self._generate_content_with_model(prompt)

    async def _generate_content_with_model(self, prompt: str) -> FastAPIStreamingResponse:
        """Generate content using the language model"""
        try:
            # Use the model to generate content based on the prompt
            response = await self.model.agenerate(
                messages=[{"role": "user", "content": prompt}]
            )
            
            content = response.generations[0][0].text
            return stream_string(content, True)
        except Exception as e:
            logger.exception(f"Error generating content with model: {str(e)}")
            return stream_string("Failed to generate content. Please try again with more specific parameters.", True)
