import asyncio
import remote_turtle

async def main():
    t = remote_turtle.RemoteTurtle()
    await t.connect()
    await t.forward()
    await t.right()
    await t.forward()
    await t.wait()

asyncio.run(main())