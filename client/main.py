import asyncio
import remote_turtle

async def main():
    t = remote_turtle.RemoteTurtle("tkilla")
    await t.connect()
    await t.straight("faster")
    await t.right("faster")
    await t.left("faster")
    await t.straight("slower")
    await t.straight("slower")
    await t.straight("slower")
    await t.wait()

asyncio.run(main())