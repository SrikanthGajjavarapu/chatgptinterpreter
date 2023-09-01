import os
os.environ["OPENAI_API_KEY"] = "here paste api key"

from codeinterpreterapi import CodeInterpreterSession, File

async def main():
    # context manager for auto start/stop of the session
    async with CodeInterpreterSession(model="gpt-3.5-turbo") as session:
        # define the user request
        user_request = "Analyze this dataset and plot close from the year 1980 to 2022."
        files = [
            File.from_path("apple.csv"),
        ]

        # generate the response
        response = await session.generate_response(
            user_request, files=files
        )

        # output to the user
        print("AI: ", response.content)
        for file in response.files:
            file.show_image()


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
