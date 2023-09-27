# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.

import typing
import commands2
import wpilib

from subsystems.drivetrain import Drivetrain


class TankDrive(commands2.CommandBase):
    def __init__(
        self, 
        drive: Drivetrain,
        leftSpeed: typing.Callable[[], float], 
        rightSpeed: typing.Callable[[], float],
    ) -> None:
        """Creates a new TankDrive. This command will drive your robot for a desired left and right motor speed."""
        super().__init__()

        self.leftSpeed = leftSpeed
        self.rightSpeed = rightSpeed
        self.drive = drive
        self.addRequirements([drive])

    def execute(self) -> None:
        """Called every time the scheduler runs while the command is scheduled."""
        self.drive.leftMotor.set(self.leftSpeed())
        self.drive.rightMotor.set(self.rightSpeed())

