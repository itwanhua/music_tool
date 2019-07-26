# 音乐播放器
import random
import os
import pygame
import time

pygame.mixer.init()
def menu():
    print("#########功能菜单#########")
    print("# 0.播放                 #")
    print("# 1.暂停                 #")
    print("# 2.继续                 #")
    print("# 3.切歌                 #")
    print("# 4.停止                 #")
    print("##########################")

def music_play(music):
    music_name = music
    try:
        pygame.mixer.music.load(r"C:/Users/wan/Desktop/music_tool/music/%s.mp3" % music_name)
        print("\n正在播放: %s" % music_name)
        pygame.mixer.music.play()
        return music_name
    except:
        pass

def pause_music():
    print("暂停播放\n")
    pygame.mixer.music.pause()

def unpause_music():
    print("继续播放\n")
    pygame.mixer.music.unpause()

def stop_music():
    print("停止播放\n")
    pygame.mixer.music.stop()

def skip_music():
    i = random.randint(0, len(music_list)-1)
    music_name = music_list[i]
    music_play(music_name)




if __name__ == "__main__":
    music_path = './music'
    music_list = []
    f = os.listdir(music_path)
    for file_name in f:
        music = file_name[:-4]
        music_list.append(music)
    menu()

    while True:
        s = input("\n输入菜单序号：")
        if s == "0":
            music_name = random.choice(music_list)
            music_play(music_name)
        elif s == "1":
            pause_music()
        elif s == "2":
            unpause_music()
        elif s == "3":
            skip_music()
        elif s == "4":
            stop_music()
            
        else:
            print("输入不合法！")

    

