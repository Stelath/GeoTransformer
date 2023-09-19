import argparse
import numpy as np
import open3d as o3d

def use_o3d(pts, write_text, output_file):
    pcd = o3d.geometry.PointCloud()

    # the method Vector3dVector() will convert numpy array of shape (n, 3) to Open3D format.
    # see http://www.open3d.org/docs/release/python_api/open3d.utility.Vector3dVector.html#open3d.utility.Vector3dVector
    pcd.points = o3d.utility.Vector3dVector(pts)

    # http://www.open3d.org/docs/release/python_api/open3d.io.write_point_cloud.html#open3d.io.write_point_cloud
    o3d.io.write_point_cloud(output_file, pcd, write_ascii=write_text)

def main(args):
    # Load the numpy pointcloud file
    pts = np.load(args.input_file)

    # Create the PlyData object
    write_text = True

    # Write the ply file
    use_o3d(pts, write_text, args.output_file)


if __name__ == '__main__':
    # Define the command line arguments
    parser = argparse.ArgumentParser(description='Convert a numpy pointcloud file to a ply file')
    parser.add_argument('-i', '--input_file', type=str, help='The input numpy file')
    parser.add_argument('-o', '--output_file', type=str, help='The output ply file')

    # Parse the command line arguments
    args = parser.parse_args()

    main(args)