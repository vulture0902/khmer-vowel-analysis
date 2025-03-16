import os
import parselmouth
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib.patches as patches
from matplotlib import font_manager
from scipy.interpolate import interp1d
from scipy.signal import medfilt

font_prop = font_manager.FontProperties(family='Khmer OS System')
font_manager.fontManager.addfont(os.path.join(os.getcwd(), "KhmerOSsys.ttf"))

def main():

    vowels = {
        'i': (250, 2350, 'white'),
        'ɪ': (350, 2050, 'white'),
        'e': (450, 1950, 'white'),
        'ɛ': (550, 1750, 'white'),
        'æ': (650, 1550, 'white'),
        'ɑ': (750, 1150, 'white'),
        'ɔ': (550, 950,  'white'),
        'o': (450, 850,  'white'),
        'ʊ': (350, 1050, 'white'),
        'u': (250, 950,  'white'),
        'ʌ': (650, 1350, 'white'),
        'ɒ': (750, 850,  'white'),
    }

    vowels_jp = {
        'A(j)': (700, 1400, 'yellow'),
        'I(j)': (250, 2200, 'yellow'),
        'U(j)': (300, 1100, 'yellow'),
        'E(j)': (500, 1900, 'yellow'),
        'O(j)': (400, 800,  'yellow'),
    }

    # https://www.youtube.com/watch?v=mBZpNL1HSOg
    mp3_file1_type1_o1 = f"{os.getcwd()}/sound_from_youtube/men_video1_time_st0006_type1_o1.wav"
    mp3_file1_type1_o2 = f"{os.getcwd()}/sound_from_youtube/men_video1_time_st0006_type1_o2.wav"
    mp3_file1_type2_o1 = f"{os.getcwd()}/sound_from_youtube/men_video1_time_st0024_type2_o1.wav"
    mp3_file1_type2_o2 = f"{os.getcwd()}/sound_from_youtube/men_video1_time_st0024_type2_o2.wav"
    mp3_file1_type3_o1 = f"{os.getcwd()}/sound_from_youtube/men_video1_time_st0103_type3_o1.wav"
    mp3_file1_type3_o2 = f"{os.getcwd()}/sound_from_youtube/men_video1_time_st0103_type3_o2.wav"

    # https://www.youtube.com/watch?v=CFUNyVSjWWQ
    mp3_file2_type1_o1 = f"{os.getcwd()}/sound_from_youtube/women_video2_time_st0137_type1_o1.wav"
    mp3_file2_type1_o2 = f"{os.getcwd()}/sound_from_youtube/women_video2_time_st0141_type1_o2.wav"
    mp3_file2_type2_o1 = f"{os.getcwd()}/sound_from_youtube/women_video2_time_st0147_type2_o1.wav"
    mp3_file2_type2_o2 = f"{os.getcwd()}/sound_from_youtube/women_video2_time_st0151_type2_o2.wav"

    # https://www.youtube.com/watch?v=NkLKdlRqVzE
    mp3_file3_type1_o1 = f"{os.getcwd()}/sound_from_youtube/men_video3_time_st0023_type1_o1.wav"
    mp3_file3_type1_o2 = f"{os.getcwd()}/sound_from_youtube/men_video3_time_st0023_type1_o2.wav"
    mp3_file3_type2_o1 = f"{os.getcwd()}/sound_from_youtube/men_video3_time_st0029_type2_o1.wav"
    mp3_file3_type2_o2 = f"{os.getcwd()}/sound_from_youtube/men_video3_time_st0029_type2_o2.wav"

    # men video1 
    plot_init(vowels)
    plot_formants(plt, mp3_file1_type1_o1, 'blue', '^', "អ")
    plot_formants(plt, mp3_file1_type2_o1, 'blue', '^', "អ")
    plot_formants(plt, mp3_file1_type3_o1, 'blue', '^', "អ")
    plot_formants(plt, mp3_file1_type1_o2, 'red',  '^', "អ៊")
    plot_formants(plt, mp3_file1_type2_o2, 'red',  '^', "អ៊")
    plot_formants(plt, mp3_file1_type3_o2, 'red',  '^', "អ៊")
    plt.savefig(f"{os.getcwd()}/fig/video1_men.png", dpi=300, bbox_inches='tight')
    plt.clf()

    # women video2 
    plot_init(vowels)
    plot_formants(plt, mp3_file2_type1_o1, 'blue', 'v', "អ")
    plot_formants(plt, mp3_file2_type2_o1, 'blue', 'v', "អ")
    plot_formants(plt, mp3_file2_type1_o2, 'red',  'v', "អ៊")
    plot_formants(plt, mp3_file2_type2_o2, 'red',  'v', "អ៊")
    plt.savefig(f"{os.getcwd()}/fig/video2_women.png", dpi=300, bbox_inches='tight')
    plt.clf()

    # men video3
    plot_init(vowels)
    plot_formants(plt, mp3_file3_type1_o1, 'blue', 's', "អ")
    plot_formants(plt, mp3_file3_type2_o1, 'blue', 's', "អ")
    #plot_formants(plt, mp3_file3_type1_o2, 'red',  's', "អ៊") not good
    plot_formants(plt, mp3_file3_type2_o2, 'red',  's', "អ៊")
    plt.savefig(f"{os.getcwd()}/fig/video3_men.png", dpi=300, bbox_inches='tight')
    plt.clf()

    # men video1
    vowels.update(vowels_jp)
    plot_init(vowels)
    plot_formants(plt, mp3_file1_type1_o1, 'blue', '^', "អ")
    plot_formants(plt, mp3_file1_type2_o1, 'blue', '^', "អ")
    plot_formants(plt, mp3_file1_type3_o1, 'blue', '^', "អ")
    plot_formants(plt, mp3_file1_type1_o2, 'red',  '^', "អ៊")
    plot_formants(plt, mp3_file1_type2_o2, 'red',  '^', "អ៊")
    plot_formants(plt, mp3_file1_type3_o2, 'red',  '^', "អ៊")
    plt.savefig(f"{os.getcwd()}/fig/video1_men_japanese.png", dpi=300, bbox_inches='tight')
    plt.clf()

def plot_init(vowels):

    plt.figure(figsize=(12, 6))
    plt.ylabel('F1')
    plt.xlabel('F2')
    plt.title('Formant Tracking')
    plt.grid(True)
    plt.xlim(300, 2700)
    plt.ylim(100, 1100)
    plt.gca().invert_xaxis()
    plt.gca().invert_yaxis()
    plot_ipa_vowels(plt, vowels)

def plot_ipa_vowels(plt, vowels):

    for vowel, (f1, f2, color) in vowels.items():
        ellipse = patches.Ellipse(xy=(f2, f1), width=200, height=100, angle=0, edgecolor='black', facecolor=color)
        plt.gca().add_patch(ellipse)
        plt.text(f2, f1, vowel, fontsize=12, ha='center', va='center')

def median_and_moving_average_filter(data, kernel_size, window_size):

  filtered_data = medfilt(data, kernel_size)
  filtered_data = np.convolve(filtered_data, np.ones(window_size), 'valid') / window_size
  return filtered_data.tolist()

def extract_formants_from_mp3(file_path):

    try:
        sound = parselmouth.Sound(file_path)
        point_process = sound.to_formant_burg(max_number_of_formants=5.0, maximum_formant=5500.0, window_length=0.025, pre_emphasis_from=50.0)

        num_points = point_process.get_number_of_frames()
        times = [point_process.get_time_from_frame_number(i+1) for i in range(num_points)]

        f1 = [point_process.get_value_at_time(1, t) for t in times]
        f2 = [point_process.get_value_at_time(2, t) for t in times]
        #f3 = [point_process.get_value_at_time(3, t) for t in times]

        kernel_size = 19
        window_size = 15
        f1_smoothed = median_and_moving_average_filter(f1, kernel_size, window_size)
        f2_smoothed = median_and_moving_average_filter(f2, kernel_size, window_size)

        return times, f1_smoothed, f2_smoothed

    except Exception as e:
        print(f"There was an error: {e}")
        return None, None, None

def plot_formants(plt, mp3_file, color, plot_type, plot_text):

    times, f1, f2 = extract_formants_from_mp3(mp3_file)

    if times is None or f1 is None or f2 is None:
      return

    plt.scatter(f2, f1, c=color, marker=plot_type)

    # Find max and min values with margin
    # Adjust this value to control the margin
    margin_factor = 1.1
    max_f1 = max(f1) * margin_factor
    min_f1 = min(f1) / margin_factor
    max_f2 = max(f2) * margin_factor
    min_f2 = min(f2) / margin_factor

    # Calculate center and axes length
    center_x = (max_f2 + min_f2) / 2
    center_y = (max_f1 + min_f1) / 2
    width = max_f2 - min_f2
    height = max_f1 - min_f1

    # Draw ellipse
    ellipse = patches.Ellipse((center_x, center_y), width, height, color=color, alpha=0.1)
    plt.gca().add_patch(ellipse)

    # Draw text
    t = plt.text(center_x,center_y, plot_text,fontsize=17,weight="bold", color=color, fontproperties=font_prop)
    t.set_bbox(dict(facecolor='white', alpha=0.5, edgecolor='gray'))

if __name__ == "__main__":
    main()
