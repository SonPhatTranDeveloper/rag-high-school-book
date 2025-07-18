import asyncio

from llama_deploy import (
    ControlPlaneConfig,
    SimpleMessageQueueConfig,
    deploy_core,
)


async def main():
    """
    Deploy core components
    """
    await deploy_core(
        control_plane_config=ControlPlaneConfig(),
        message_queue_config=SimpleMessageQueueConfig(),
    )


if __name__ == "__main__":
    asyncio.run(main())
