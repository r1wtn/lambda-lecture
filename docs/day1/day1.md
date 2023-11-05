# Day1

## 前提

- Python FastAPI(またはFlask)でAPIの実装をしたことがある。

## 目的

- FastAPIと同じノリでLambdaも作れるようになる。
  - `Powertools for AWS Lambda` を利用します。
  - https://docs.powertools.aws.dev/lambda/python/latest/
  - FastAPIで提供される設計が非常に良いため、(Router, PydanticによるValidation, Dependency Injection) APIGateway+Lambdaの構成においても同様の構成で作れたら幸せです。
- 設計 → 実装 → テスト という一覧の流れを1人でできるようにする。



## 勉強項目

- 速く・きれいに書くには。
  - VSCodeに予測変換してもらえるコードを書く。
  - Github Copilot に予測してもらえるコードを書く。
- クライアントからのリクエストをどのように受け取るのか。
- API Gateway から受け取るデータのフォーマットはどのようになっているか。
- 各種パラメータはどうやって取得すればいいか。
- レスポンスはどのように返せばいいか。
- Validationをどのように実装すればきれいに書けるか。
- レスポンスはどのように書けばきれいに書けるか。
- `datetime` などjsonableじゃないオブジェクトはどうやって処理するか。
- テストコードはどのタイミングで書くべきか.
- テストコードを格納するフォルダはどのような構成であるべきか。
- fixture のスコープをどのように考えればいいか。
- テスト用のデータをどうやって作成すればいいか。
