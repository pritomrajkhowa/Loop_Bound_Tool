PREFIX=/usr
CC=gcc
CXX=g++
CXXFLAGS= -D_MP_INTERNAL -D_AMD64_ -D_USE_THREAD_LOCAL -DNDEBUG -D_EXTERNAL_RELEASE  -std=c++11 -fvisibility=hidden -c -mfpmath=sse -msse -msse2 -fopenmp -O3 -D _EXTERNAL_RELEASE -fomit-frame-pointer -D_LINUX_ -fPIC
EXAMP_DEBUG_FLAG=
CXX_OUT_FLAG=-o 
OBJ_EXT=.o
LIB_EXT=.a
AR=ar
AR_FLAGS=rcs
AR_OUTFLAG=
EXE_EXT=
LINK=g++
LINK_FLAGS=
LINK_OUT_FLAG=-o 
LINK_EXTRA_FLAGS=-lpthread  -fopenmp -lrt
SO_EXT=.so
SLINK=g++
SLINK_FLAGS=-shared
SLINK_EXTRA_FLAGS= -fopenmp -lrt
SLINK_OUT_FLAG=-o 
OS_DEFINES=-D_LINUX_
