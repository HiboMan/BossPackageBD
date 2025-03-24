from typing import TYPE_CHECKING

from carfigures.packages.boss.cog import Boss

if TYPE_CHECKING:
    from carfigures.core.bot import CarFiguresBot


async def setup(bot: "CarFiguresBot"):
    await bot.add_cog(Boss(bot))
