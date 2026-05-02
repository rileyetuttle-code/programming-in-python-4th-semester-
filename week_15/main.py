import datetime as dt

import pygame as pg

import solar_system as ss


def main() -> None: 
    """Planet Simulation by Riley Tuttle"""
    # Starting parameters
    start_date: str = "2026-04-28"
    window_size: int = 800
    fps: int = 120

    # Pygame setup
    pg.init()
    pg.display.set_caption("Planet Simulation by Riley Tuttle")
    screen: pg.Surface = pg.display.set_mode((window_size, window_size))
    clock: pg.time.Clock = pg.time.Clock()

    # Simulation setup
    current_date: dt.datetime = dt.datetime.strptime(start_date, r"%Y-%m-%d")
    solar_system: ss.SolarSystem = ss.SolarSystem(current_date, "solar_bodies.csv")

    # Main Loop
    running: bool = True
    while running: 
        # Ticks
        clock.tick(fps)

        # Events
        for event in pg.event.get(): 
            if event.type == pg.QUIT: 
                running = False

        # Physics
        # Graphics


if __name__ == "__main__":
    main()