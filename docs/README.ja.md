# 🚀 MirageMask  
✨ **概要説明**: Windows向けのレッドチームテストツールライブラリ。トロイの木馬の偽装機能を専門とする。  
[![Release](https://img.shields.io/github/v/release/yourname/project)](https://github.com/yourname/project)  
[![CI/CD](https://img.shields.io/github/actions/workflow/status/yourname/project/build.yml)](https://github.com/yourname/project/actions)  
![プレビュー](back.png)  

## 🌐 言語  
- [English](README.en.md)  
- [简体中文](README.md)  
- [Español](README.es.md)  
- [日本語](README.ja.md)  

## ⚠️ **法的免責事項**  
```text  
• 本ツールは**法的に認可されたセキュリティテスト**に限定して使用すること。  
  禁止される用途:  
  ⛔ 無許可の侵入テスト | ⛔ DDoS攻撃 | ⛔ データ窃取  
• 中国刑法第285条及びサイバーセキュリティ法第27条への準拠は利用者の責任とする  
• 開発者は本ツールの不正使用による民事/刑事責任を**一切負わない**  


  
詳細は [法的通知](../legal/DISCLAIMER.md) を参照  
```

## 🌟 機能  
- ✅ Windowsファイルの任意偽装  
- 🚄 大規模ファイルエントリーポイントハイジャック  
**開発予定機能**  
- 🔒 ファイルからのアイコン抽出  
- 🔒 EXEアイコン変更  

## 🔰 UIプレビュー  
![プレビュー](seeUI.png)  

## 🛠️ クイックスタート  
### 前提条件  
```bash  
python 3.8+  
pyinstaller  
```

  

### インストール  
```bash  
git clone https://github.com/yourname/project.git  
pip install -r requirements.txt  
pip install pyinstaller  
```

  

## 🤝 コントリビューション  
1. リポジトリをフォーク  
2. 機能ブランチを作成  
3. 変更をコミット  
4. ブランチにプッシュ  
5. プルリクエストを送信  

## 📜 ライセンス  
[Apache 2.0](LICENSE) ライセンスで提供  

---  
## ⭐ 作者のBilibili  
【深山でコードを書く漠猫のBilibili】 [https://b23.tv/nKcZ1pB ](https://b23.tv/nKcZ1pB ) 

---  
## ⚜️ クレジット  
UIテンプレート: [PyDracula](https://github.com/Wanderson-Magalhaes/PyDracula)  

## ⚠️ カスタマイズ注意事項  
- バンドルコードは `/Trojans` ディレクトリに格納  
- 検出回避のため最小限の実装を採用  
- 実戦環境(例: ネットワーク防衛演習)では追加の暗号化/難読化/逆解析対策が必要  
- アンチVM/デバッグ機能を追加することで良性アプリケーションとの識別困難性を向上  
