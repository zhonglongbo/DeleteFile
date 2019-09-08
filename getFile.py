# -*- coding: utf-8 -*-
import os
for fpathe,dirs,fs in os.walk('/root'):
  for f in fs:
    print os.path.join(fpathe,f)