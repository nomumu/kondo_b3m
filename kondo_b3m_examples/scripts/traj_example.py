#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import math
import rospy
import actionlib
from control_msgs.msg import (FollowJointTrajectoryAction,FollowJointTrajectoryGoal,JointTolerance)
from trajectory_msgs.msg import JointTrajectoryPoint

class TestTraj(object):
    def __init__(self):
        self.__client = actionlib.SimpleActionClient("/b3m/pos_traj_control/follow_joint_trajectory",
                                                     FollowJointTrajectoryAction)
        if not self.__client.wait_for_server(rospy.Duration(3.0)):
            rospy.logerr("Trajectory action server not found.")
            rospy.signal_shutdown("exit")
            rospy.spin()

    def get_tolerance(self,name):
        # Allowed to move without restriction
        result = JointTolerance()
        result.name = name
        result.position = -1
        result.velocity = -1
        result.acceleration = -1
        return result

    def req_desired_rad(self, start_rad, end_rad, goal_sec):
        goal = FollowJointTrajectoryGoal()
        goal.trajectory.joint_names = ["joint1","joint2"]

        # Start trajectory
        traj_point = JointTrajectoryPoint()
        traj_point.positions.append(start_rad)  # joint1
        traj_point.positions.append(start_rad)  # joint2
        traj_point.time_from_start = rospy.Duration(nsecs=1)
        goal.trajectory.points.append(traj_point)

        # End trajectory
        traj_point = JointTrajectoryPoint()
        traj_point.positions.append(end_rad)    # joint1
        traj_point.positions.append(end_rad)    # joint2
        traj_point.time_from_start = rospy.Duration(goal_sec)
        goal.trajectory.points.append(traj_point)
        
        # Set tolerance
        goal.goal_tolerance.append(self.get_tolerance("joint1"))
        goal.goal_tolerance.append(self.get_tolerance("joint2"))

        # Run
        self.__client.send_goal(goal)
        self.__client.wait_for_result(rospy.Duration(goal_sec+1))
        return self.__client.get_result()

if __name__ == '__main__':
    rospy.init_node("test_traj_node")

    tt = TestTraj()
    if rospy.is_shutdown():
        sys.exit(1)

    # Test angle list[deg]
    test_angle=[0,90,0,-90,0]
    last_rad=0
    for angle in test_angle:
        # deg => rad
        start_rad=last_rad
        end_rad=math.radians(angle)
        # Request
        tt.req_desired_rad(start_rad,end_rad,1.0)
        last_rad=end_rad
        # Wait
        rospy.sleep(1.0)

