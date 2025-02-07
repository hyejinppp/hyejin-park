#!/bin/bash

# analyze.py 실행하고 결과를 log.txt로 저장
python analyze.py > log.txt 2>&1

# 확인을 위한 메시지 출력
echo "This is a test log message" >> log.txt
echo "Analysis complete. Check log.txt for details."