import yt
import glob
import os

file_list = sorted(glob.glob("hdf5/BinaryBHPlot_*.3d.hdf5"))

output_dir = "frames"
os.makedirs(output_dir, exist_ok=True)

for i, filename in enumerate(file_list):
    ds = yt.load(filename)
    slice_plot = yt.SlicePlot(ds, "z", "chi")  
    slice_plot.set_cmap("chi", "viridis")
    slice_plot.annotate_timestamp(corner='upper_left')
    output_file = os.path.join(output_dir, f"frame_{i:04d}.png")
    slice_plot.save(output_file)

