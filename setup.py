from setuptools import setup

setup(
    name="ai_custom_utils",
    version="0.0.1",
    description="AI Custom Utils",
    url="",
    author="Davos Code",
    author_email="jdhernandez@azzertai.com",
    license="MIT",
    packages=[
        "ai_custom_utils", 
        "ai_custom_utils.agentic_patterns.planning_pattern", 
        "ai_custom_utils.agentic_patterns.multiagent_pattern", 
        "ai_custom_utils.agentic_patterns.tool_pattern", 
        "ai_custom_utils.agentic_patterns.reflection_pattern",
        "ai_custom_utils.agentic_patterns.utils"
    ],
    zip_safe=False,
)
