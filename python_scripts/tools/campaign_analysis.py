from typing import Any, Dict, List, Optional
import json

from fastapi.responses import StreamingResponse as FastAPIStreamingResponse
from loguru import logger

from reworkd_platform.web.api.agent.stream_mock import stream_string
from reworkd_platform.web.api.agent.tools.reason import Reason
from reworkd_platform.web.api.agent.tools.tool import Tool
from reworkd_platform.schemas.user import UserBase
from reworkd_platform.db.crud.oauth import OAuthCrud

class CampaignAnalysis(Tool):
    description = (
        "Analyze marketing campaign performance, identify optimization opportunities, "
        "and provide recommendations for improving conversion rates.\n"
    )
    public_description = "Analyze marketing campaigns and optimize for better performance."
    arg_description = "The campaign details, metrics, goals, and specific aspects to analyze."
    image_url = "/tools/analytics.png"

    async def call(
        self, goal: str, task: str, input_str: str, user: UserBase, oauth_crud: OAuthCrud, *args: Any, **kwargs: Any
    ) -> FastAPIStreamingResponse:
        try:
            # Parse the input to extract campaign analysis parameters
            campaign_params = self._parse_campaign_parameters(input_str)
            
            # Generate the appropriate analysis based on the campaign type
            if campaign_params["type"].lower() in ["social", "social media"]:
                return await self._analyze_social_campaign(goal, task, campaign_params)
            elif campaign_params["type"].lower() in ["email", "newsletter"]:
                return await self._analyze_email_campaign(goal, task, campaign_params)
            elif campaign_params["type"].lower() in ["seo", "search", "organic"]:
                return await self._analyze_seo_campaign(goal, task, campaign_params)
            elif campaign_params["type"].lower() in ["ppc", "paid", "ads", "advertising"]:
                return await self._analyze_paid_campaign(goal, task, campaign_params)
            elif campaign_params["type"].lower() in ["affiliate", "partner"]:
                return await self._analyze_affiliate_campaign(goal, task, campaign_params)
            else:
                # Default to general campaign analysis
                return await self._analyze_general_campaign(goal, task, campaign_params)
            
        except Exception as e:
            logger.exception(f"Error in campaign analysis: {str(e)}")
            return await Reason(self.model, self.language).call(
                goal, task, input_str, user, oauth_crud, *args, **kwargs
            )

    def _parse_campaign_parameters(self, input_str: str) -> dict:
        """Parse the input string to extract campaign analysis parameters"""
        # Default parameters
        params = {
            "type": "general",
            "metrics": [],
            "goals": [],
            "timeframe": "recent",
            "focus": "general"
        }
        
        # Try to extract campaign type
        campaign_types = ["social", "social media", "email", "newsletter", "seo", "search", 
                         "organic", "ppc", "paid", "ads", "advertising", "affiliate", "partner"]
        for camp_type in campaign_types:
            if camp_type in input_str.lower():
                params["type"] = camp_type
                break
        
        # Extract metrics if mentioned
        metrics = ["impressions", "clicks", "ctr", "conversion", "roi", "engagement", 
                  "reach", "bounce rate", "time on page", "open rate", "cpc", "cpa"]
        params["metrics"] = [metric for metric in metrics if metric in input_str.lower()]
        
        # Extract goals if mentioned
        goals = ["increase sales", "lead generation", "brand awareness", "traffic", 
                "engagement", "retention", "conversion"]
        params["goals"] = [goal for goal in goals if goal in input_str.lower()]
        
        # Extract timeframe if mentioned
        timeframes = ["day", "week", "month", "quarter", "year", "recent"]
        for timeframe in timeframes:
            if timeframe in input_str.lower():
                params["timeframe"] = timeframe
                break
        
        # Extract focus area if mentioned
        focus_areas = ["performance", "optimization", "audience", "creative", 
                      "budget", "targeting", "messaging", "general"]
        for focus in focus_areas:
            if focus in input_str.lower():
                params["focus"] = focus
                break
        
        return params

    async def _analyze_social_campaign(self, goal: str, task: str, params: dict) -> FastAPIStreamingResponse:
        """Analyze social media campaign performance"""
        prompt = f"""
        Analyze a social media marketing campaign with the following parameters:
        
        Metrics to focus on: {', '.join(params['metrics']) if params['metrics'] else 'All relevant metrics'}
        Campaign goals: {', '.join(params['goals']) if params['goals'] else 'General performance'}
        Timeframe: {params['timeframe']}
        Focus area: {params['focus']}
        
        Provide:
        1. A comprehensive analysis of the campaign performance
        2. Key insights and patterns identified
        3. Specific optimization recommendations for:
           - Content strategy
           - Audience targeting
           - Posting schedule
           - Engagement tactics
           - Platform-specific optimizations
        4. Actionable next steps to improve performance
        
        Goal: {goal}
        Task: {task}
        """
        
        return await self._generate_analysis_with_model(prompt)

    async def _analyze_email_campaign(self, goal: str, task: str, params: dict) -> FastAPIStreamingResponse:
        """Analyze email campaign performance"""
        prompt = f"""
        Analyze an email marketing campaign with the following parameters:
        
        Metrics to focus on: {', '.join(params['metrics']) if params['metrics'] else 'Open rate, click-through rate, conversion rate'}
        Campaign goals: {', '.join(params['goals']) if params['goals'] else 'General performance'}
        Timeframe: {params['timeframe']}
        Focus area: {params['focus']}
        
        Provide:
        1. A comprehensive analysis of the email campaign performance
        2. Key insights on subscriber behavior and engagement
        3. Specific optimization recommendations for:
           - Subject lines
           - Email content and design
           - Call-to-action effectiveness
           - Segmentation strategy
           - Send time optimization
        4. A/B testing suggestions for future campaigns
        
        Goal: {goal}
        Task: {task}
        """
        
        return await self._generate_analysis_with_model(prompt)

    async def _analyze_seo_campaign(self, goal: str, task: str, params: dict) -> FastAPIStreamingResponse:
        """Analyze SEO campaign performance"""
        prompt = f"""
        Analyze an SEO/organic search campaign with the following parameters:
        
        Metrics to focus on: {', '.join(params['metrics']) if params['metrics'] else 'Rankings, organic traffic, conversions'}
        Campaign goals: {', '.join(params['goals']) if params['goals'] else 'General performance'}
        Timeframe: {params['timeframe']}
        Focus area: {params['focus']}
        
        Provide:
        1. A comprehensive analysis of the SEO campaign performance
        2. Key insights on keyword rankings and content effectiveness
        3. Specific optimization recommendations for:
           - On-page SEO factors
           - Content strategy
           - Technical SEO improvements
           - Backlink profile
           - User experience factors affecting SEO
        4. Competitive analysis and gap identification
        
        Goal: {goal}
        Task: {task}
        """
        
        return await self._generate_analysis_with_model(prompt)

    async def _analyze_paid_campaign(self, goal: str, task: str, params: dict) -> FastAPIStreamingResponse:
        """Analyze paid advertising campaign performance"""
        prompt = f"""
        Analyze a paid advertising campaign with the following parameters:
        
        Metrics to focus on: {', '.join(params['metrics']) if params['metrics'] else 'CPC, CTR, conversion rate, ROAS'}
        Campaign goals: {', '.join(params['goals']) if params['goals'] else 'General performance'}
        Timeframe: {params['timeframe']}
        Focus area: {params['focus']}
        
        Provide:
        1. A comprehensive analysis of the paid campaign performance
        2. Key insights on ad effectiveness and audience response
        3. Specific optimization recommendations for:
           - Ad creative and copy
           - Audience targeting
           - Bid strategy
           - Budget allocation
           - Landing page optimization
        4. ROI analysis and suggestions for improving cost efficiency
        
        Goal: {goal}
        Task: {task}
        """
        
        return await self._generate_analysis_with_model(prompt)

    async def _analyze_affiliate_campaign(self, goal: str, task: str, params: dict) -> FastAPIStreamingResponse:
        """Analyze affiliate marketing campaign performance"""
        prompt = f"""
        Analyze an affiliate marketing campaign with the following parameters:
        
        Metrics to focus on: {', '.join(params['metrics']) if params['metrics'] else 'Clicks, conversions, commission, EPC'}
        Campaign goals: {', '.join(params['goals']) if params['goals'] else 'General performance'}
        Timeframe: {params['timeframe']}
        Focus area: {params['focus']}
        
        Provide:
        1. A comprehensive analysis of the affiliate campaign performance
        2. Key insights on partner performance and conversion patterns
        3. Specific optimization recommendations for:
           - Partner selection and management
           - Commission structure
           - Promotional materials
           - Conversion funnel optimization
           - Compliance and tracking
        4. Strategies for scaling successful affiliate relationships
        
        Goal: {goal}
        Task: {task}
        """
        
        return await self._generate_analysis_with_model(prompt)

    async def _analyze_general_campaign(self, goal: str, task: str, params: dict) -> FastAPIStreamingResponse:
        """Analyze general marketing campaign performance"""
        prompt = f"""
        Analyze a marketing campaign with the following parameters:
        
        Metrics to focus on: {', '.join(params['metrics']) if params['metrics'] else 'All relevant metrics'}
        Campaign goals: {', '.join(params['goals']) if params['goals'] else 'General performance'}
        Timeframe: {params['timeframe']}
        Focus area: {params['focus']}
        
        Provide:
        1. A comprehensive analysis of the campaign performance
        2. Key insights and patterns identified
        3. Specific optimization recommendations for:
           - Targeting and audience segmentation
           - Messaging and creative elements
           - Channel selection and budget allocation
           - Conversion funnel optimization
           - Testing and iteration strategy
        4. Actionable next steps to improve performance
        
        Goal: {goal}
        Task: {task}
        """
        
        return await self._generate_analysis_with_model(prompt)

    async def _generate_analysis_with_model(self, prompt: str) -> FastAPIStreamingResponse:
        """Generate analysis using the language model"""
        try:
            # Use the model to generate analysis based on the prompt
            response = await self.model.agenerate(
                messages=[{"role": "user", "content": prompt}]
            )
            
            analysis_content = response.generations[0][0].text
            return stream_string(analysis_content, True)
        except Exception as e:
            logger.exception(f"Error generating analysis with model: {str(e)}")
            return stream_string("Failed to generate campaign analysis. Please try again with more specific parameters.", True)
