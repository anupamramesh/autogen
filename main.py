import autogen
from autogen import AssistantAgent, UserProxyAgent

def main():
    config_list = [
        {
            'model': 'gpt-3.5-turbo',
            "api_key": "xxx"
        }
    ]

    assistant = autogen.AssistantAgent(
        name="Assistant",
        llm_config={
            "config_list": config_list
        }
    )

    user_proxy = autogen.UserProxyAgent(
        name="user",
        human_input_mode="ALWAYS",
        code_execution_config={
            "work_dir": "coding",
            "use_docker": False
        }
    )

    user_proxy.initiate_chat(assistant, message="Plot a chart of META and TESLA stock price change.")


if __name__ == "__main__":
    main()
