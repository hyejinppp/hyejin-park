##!/bin/bash

# Git 프로젝트 디렉토리로 이동
cd ~/project_root/analyze  # 또는 실제 경로로 수정

# Git 상태 확인
echo "Checking Git status..."
git status

# 변경 사항 스테이징
echo "Staging changes..."
git add .

# 커밋
echo "Committing changes..."
git commit -m "Update files"

# GitHub에 푸시
echo "Pushing to GitHub..."
git push origin main

# 완료 메시지
echo "Upload to GitHub complete!"
