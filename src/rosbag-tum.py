import rosbag
topic =  '/camera_pose'
bagname = '../../raw_data/dataset_2/openvslam/open_2_5.bag'

def extract(bagfile, pose_topic, msg_type, out_filename):
    n = 0
    f = open(out_filename, 'w')
    f.write('# timestamp tx ty tz qx qy qz qw\n')
    with rosbag.Bag(bagfile, 'r') as bag:
        for (topic, msg, ts) in bag.read_messages(topics=str(pose_topic)):
            if msg_type == "PoseWithCovarianceStamped":
                f.write('%.12f %.12f %.12f %.12f %.12f %.12f %.12f %.12f\n' %
                        (msg.header.stamp.to_sec(),
                         msg.pose.pose.position.x, msg.pose.pose.position.y,
                         msg.pose.pose.position.z,
                         msg.pose.pose.orientation.x,
                         msg.pose.pose.orientation.y,
                         msg.pose.pose.orientation.z,
                         msg.pose.pose.orientation.w))
            elif msg_type == "PoseStamped":
                f.write('%.12f %.12f %.12f %.12f %.12f %.12f %.12f %.12f\n' %
                        (msg.header.stamp.to_sec(),
                         msg.pose.position.x, msg.pose.position.y,
                         msg.pose.position.z,
                         msg.pose.orientation.x, msg.pose.orientation.y,
                         msg.pose.orientation.z, msg.pose.orientation.w))
            else:
                assert False, "Unknown message type"
            n += 1
    print('wrote ' + str(n) + ' imu messages to the file: ' + out_filename) 


if __name__ == '__main__':
    extract(bagname,topic,"PoseStamped", "tum_open_2_5.txt")
    