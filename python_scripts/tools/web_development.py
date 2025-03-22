from typing import Any, Dict, List, Optional
import json

from fastapi.responses import StreamingResponse as FastAPIStreamingResponse
from loguru import logger

from reworkd_platform.web.api.agent.stream_mock import stream_string
from reworkd_platform.web.api.agent.tools.reason import Reason
from reworkd_platform.web.api.agent.tools.tool import Tool
from reworkd_platform.schemas.user import UserBase
from reworkd_platform.db.crud.oauth import OAuthCrud

class WebDevelopment(Tool):
    description = (
        "Generate code for web applications, landing pages, and marketing components "
        "using React, Next.js, and modern web technologies.\n"
    )
    public_description = "Create web applications and landing pages with modern frameworks."
    arg_description = "The type of web component to create (landing page, form, component), design requirements, and functionality needed."
    image_url = "/tools/code.png"

    async def call(
        self, goal: str, task: str, input_str: str, user: UserBase, oauth_crud: OAuthCrud, *args: Any, **kwargs: Any
    ) -> FastAPIStreamingResponse:
        try:
            # Parse the input to extract web development parameters
            web_params = self._parse_web_parameters(input_str)
            
            # Generate the appropriate code based on the component type
            if web_params["type"].lower() in ["landing page", "landing", "page"]:
                return await self._generate_landing_page(goal, task, web_params)
            elif web_params["type"].lower() in ["form", "lead form", "contact form"]:
                return await self._generate_form(goal, task, web_params)
            elif web_params["type"].lower() in ["component", "ui component", "react component"]:
                return await self._generate_component(goal, task, web_params)
            elif web_params["type"].lower() in ["nextjs", "next.js", "next app", "application"]:
                return await self._generate_nextjs_app(goal, task, web_params)
            else:
                # Default to general web component
                return await self._generate_general_component(goal, task, web_params)
            
        except Exception as e:
            logger.exception(f"Error in web development: {str(e)}")
            return await Reason(self.model, self.language).call(
                goal, task, input_str, user, oauth_crud, *args, **kwargs
            )

    def _parse_web_parameters(self, input_str: str) -> dict:
        """Parse the input string to extract web development parameters"""
        # Default parameters
        params = {
            "type": "component",
            "design": "modern",
            "features": [],
            "framework": "react",
            "responsive": True,
            "seo": True
        }
        
        # Try to extract component type
        component_types = ["landing page", "landing", "page", "form", "lead form", 
                          "contact form", "component", "ui component", "react component",
                          "nextjs", "next.js", "next app", "application"]
        for comp_type in component_types:
            if comp_type in input_str.lower():
                params["type"] = comp_type
                break
        
        # Extract framework preference
        frameworks = ["react", "next.js", "nextjs", "tailwind"]
        for framework in frameworks:
            if framework in input_str.lower():
                params["framework"] = framework
                break
        
        # Extract design preferences
        design_styles = ["modern", "minimalist", "bold", "colorful", "professional", "corporate"]
        for style in design_styles:
            if style in input_str.lower():
                params["design"] = style
                break
        
        # Extract features
        feature_keywords = ["form", "animation", "gallery", "slider", "testimonial", 
                           "pricing", "navigation", "footer", "header", "hero", 
                           "contact", "about", "services", "portfolio", "blog"]
        params["features"] = [keyword for keyword in feature_keywords if keyword in input_str.lower()]
        
        return params

    async def _generate_landing_page(self, goal: str, task: str, params: dict) -> FastAPIStreamingResponse:
        """Generate code for a landing page"""
        prompt = f"""
        Create a complete landing page using {params['framework']} with a {params['design']} design style.
        
        The landing page should include:
        1. A responsive navigation bar
        2. A hero section with a compelling headline and call-to-action
        3. Feature sections highlighting key benefits
        4. Testimonial section (if appropriate)
        5. Contact or lead capture form
        6. Footer with necessary links and information
        
        Additional features to include: {', '.join(params['features']) if params['features'] else 'None specified'}
        
        Make sure the code is:
        - Well-structured and organized
        - Fully responsive for all device sizes
        - Optimized for SEO
        - Using modern best practices
        - Ready to be deployed
        
        Provide the complete code with clear comments explaining each section.
        
        Goal: {goal}
        Task: {task}
        """
        
        return await self._generate_code_with_model(prompt)

    async def _generate_form(self, goal: str, task: str, params: dict) -> FastAPIStreamingResponse:
        """Generate code for a form component"""
        prompt = f"""
        Create a {params['design']} style form component using {params['framework']}.
        
        The form should include:
        1. Appropriate input fields for a {params['type']}
        2. Form validation
        3. Submission handling
        4. Success/error messaging
        5. Responsive design
        
        Additional features to include: {', '.join(params['features']) if params['features'] else 'None specified'}
        
        Make sure the code:
        - Follows best practices for accessibility
        - Includes proper validation and error handling
        - Has a clean, user-friendly design
        - Is fully functional and ready to integrate
        
        Provide the complete code with clear comments explaining the functionality.
        
        Goal: {goal}
        Task: {task}
        """
        
        return await self._generate_code_with_model(prompt)

    async def _generate_component(self, goal: str, task: str, params: dict) -> FastAPIStreamingResponse:
        """Generate code for a UI component"""
        prompt = f"""
        Create a reusable {params['design']} style UI component using {params['framework']}.
        
        The component should:
        1. Be well-structured and reusable
        2. Accept appropriate props for customization
        3. Include proper TypeScript types (if applicable)
        4. Follow component best practices
        5. Be responsive and accessible
        
        Additional features to include: {', '.join(params['features']) if params['features'] else 'None specified'}
        
        Make sure the code:
        - Is clean and well-documented
        - Follows modern component patterns
        - Handles edge cases appropriately
        - Is ready to be integrated into a larger application
        
        Provide the complete code with clear comments explaining the functionality.
        
        Goal: {goal}
        Task: {task}
        """
        
        return await self._generate_code_with_model(prompt)

    async def _generate_nextjs_app(self, goal: str, task: str, params: dict) -> FastAPIStreamingResponse:
        """Generate code for a Next.js application structure"""
        prompt = f"""
        Create a Next.js application structure for a marketing-focused web application.
        
        The application should include:
        1. Project structure following Next.js best practices
        2. Key pages and components needed for a marketing site
        3. Routing configuration
        4. Basic styling setup (preferably with Tailwind CSS)
        5. SEO optimization
        
        Additional features to include: {', '.join(params['features']) if params['features'] else 'None specified'}
        
        Provide:
        1. The directory structure
        2. Key file contents with code
        3. Instructions for setup and deployment
        4. Explanation of the architecture decisions
        
        Make sure the code follows the latest Next.js standards and is optimized for performance and SEO.
        
        Goal: {goal}
        Task: {task}
        """
        
        return await self._generate_code_with_model(prompt)

    async def _generate_general_component(self, goal: str, task: str, params: dict) -> FastAPIStreamingResponse:
        """Generate code for a general web component"""
        prompt = f"""
        Create a web component based on the following description: {task}
        
        Using {params['framework']} with a {params['design']} design style.
        
        The component should:
        1. Be well-structured and functional
        2. Follow best practices for the chosen framework
        3. Be responsive and accessible
        4. Include appropriate styling
        
        Additional features to include: {', '.join(params['features']) if params['features'] else 'None specified'}
        
        Provide the complete code with clear comments explaining the functionality.
        
        Goal: {goal}
        Task: {task}
        """
        
        return await self._generate_code_with_model(prompt)

    async def _generate_code_with_model(self, prompt: str) -> FastAPIStreamingResponse:
        """Generate code using the language model"""
        try:
            # Use the model to generate code based on the prompt
            response = await self.model.agenerate(
                messages=[{"role": "user", "content": prompt}]
            )
            
            code_content = response.generations[0][0].text
            return stream_string(code_content, True)
        except Exception as e:
            logger.exception(f"Error generating code with model: {str(e)}")
            return stream_string("Failed to generate code. Please try again with more specific parameters.", True)
