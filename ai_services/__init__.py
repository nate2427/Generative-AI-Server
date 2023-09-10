# Setup OpenAI Agent
from llama_index.tools.tool_spec.load_and_search.base import LoadAndSearchToolSpec
from llama_hub.tools.yelp.base import YelpToolSpec
from llama_index.agent import OpenAIAgent
import openai
from pprint import pprint
from . import culture_trip_ai

import os
from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openai.api_key = OPENAI_API_KEY

# Import and initialize our tool spec

CULTURE_TRIP_AI_YELP_API_KEY = os.getenv("CULTURE_TRIP_AI_YELP_API_KEY")
CULTURE_TRIP_AI_YELP_CLIENT = os.getenv("CULTURE_TRIP_AI_YELP_CLIENT")

yelp_tool_spec = YelpToolSpec(api_key=CULTURE_TRIP_AI_YELP_API_KEY,
                              client_id=CULTURE_TRIP_AI_YELP_CLIENT)

# Add tools to Agent
yelp_tools = yelp_tool_spec.to_tool_list()
data_service_agent = OpenAIAgent.from_tools(
    [
        *LoadAndSearchToolSpec.from_defaults(yelp_tools[0]).to_tool_list(),
        *LoadAndSearchToolSpec.from_defaults(yelp_tools[1]).to_tool_list()
    ],
    verbose=False
)


def init_ai_services():
    from . import culture_trip_ai


# init_ai_services()
