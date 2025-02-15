# Copyright (C) 2016-2021 Alibaba Group Holding Limited
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import random
import gmpy2

def powmod(a, b, c):
  return int(gmpy2.powmod(a, b, c))


def invert(a, b):
  x = int(gmpy2.invert(a, b))
  if x == 0:
    raise ZeroDivisionError('invert(a, b) no inverse exists')
  return x
   
   
def getprimeover(n):
  r = gmpy2.mpz(random.SystemRandom().getrandbits(n))
  r = gmpy2.bit_set(r, n - 1)
  return int(gmpy2.next_prime(r))
