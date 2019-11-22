# -*- coding: utf-8 -*-
# @Time    : 19-4-23 下午5:01
# @Author  : Redtree
# @File    : amr2wav.py
# @Desc :

# -*- coding: utf-8 -*-
# @Time    : 18-8-14 下午3:16
# @Author  : Redtree
# @File    : amr2wav.py
# @Desc : 基于shell+ffmpeg的音频处理工具

import os
from pydub import AudioSegment

def amrtowav(amr_path,wav_path):
    try:
       res = os.system('ffmpeg -y -i '+amr_path+' -ar 16000 -ac 1 '+wav_path)
       if res==0:
           return 'success'
       else:
           return 'error'
    except Exception as err:
        print('音频转换失败:'+str(err))
        return 'error'

def new_amr2wav (amr_path,wav_path):
    try:
        sound = AudioSegment.from_file(amr_path)
        mono = sound.set_frame_rate(16000).set_channels(1)
        mono.export(wav_path, format="wav")
    except Exception as err:
        print('音频转换失败:'+str(err))
        return 'error'
    return 'success'

#amrtowav('rep.amr','old.wav')
#new_amr2wav('tmp.amr','new.wav')
#duration_in_milliseconds = len(sound1)
