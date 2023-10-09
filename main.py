



import os


class ffmpeg_converter:
    def __init__(self):

        self.input_directory=""
        self.output_directory=""
        self.file_name=""

    def get_input_output_directory(self):

        self.input_directory=input("please insert the video input  directory:")
        self.output_directory=input("please insert the video putput directory:")
        self.file_name=input("please insert the file name")


    def print_directories(self):

        print(self.input_directory)
        print(self.output_directory)
    def run_command(self):



        os.system("ffmpeg -i"+self.file_name+".mp4 -b:v 1M -g 60 -hls_time 2 -hls_list_size 0 -hls_segment_size 500000 output.m3u8")







if __name__ == '__main__':

    x=ffmpeg_converter()
    x.get_input_output_directory()
    x.print_directories()


