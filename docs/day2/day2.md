# Day2

## OpenAPI

### 仕様書の構造

- まずは構造を理解しましょう。
- OpenAPI の仕様は、 **めちゃめちゃネストの深い JSON** だと考えてください。
- OpenAPI は、API エンドポイントに対応する `path` から全てが始まります。
- この path に対して、 `GET`, `POST` などの `op` (operation) を定義します。
- その `op` がもつ `parameters`, `requestBody`, `responses` を定義します。
- それぞれについては、別節で詳しく解説します。

```
path/
  - op/    # GET, POST など
    - parameters/    # Header, Path, Query すべて共通です。
      - schema/
        - properties/
          - property/
            - type    # ここがobjectの場合、schemaで更にネストが深くなります。
            - schema/
              - ...
    - resquestBody/
      - schema/
        - properties/
          - ...
    - responses/
      - 200/
      - 400/
      - 500/
```

### path

- API のエンドポイントに対応します。
- 例えば `app.sample.com` にホスティングされた API サーバー があったとして、 path に `/order` を指定すると、 `https://app.sample.com/order` で対応する API にアクセスすることができます。

- サンプルを見てみましょう。

```yaml
paths:
  /order:
    $ref: ./paths/order.yaml#/order
```

- `paths` は object 型で、 `/order` が key, `$ref: ./paths/order.yaml#/order` の部分が value です。json に直すと、

```json
{
  "paths": {
    "/order": "$ref: ./paths/order.yaml#/order"
  }
}
```

- `$ref: ./paths/order.yaml#/order` の記述は、 `/order` に対応する value を別ファイルに書いているよ、という意味になります。

- その別ファイルは、 `spec/paths/order.yaml` で、さらに `#/order` で、そのファイルに定義されたオブジェクト `order` を参照してくれ、という意味になります。

- `order` も object 型になっていることがわかります。JSON に直すと、以下のとおりです。

```json
{
  "get": {
    "summary": "注文の一覧を取得する",
    "operationId": "getOrders",
    "parameters": [...]
  },
  "post": {
    ...
  }
}
```

- `path` object の key は、`get`, `post`, `patch`, `put` などのリクエストメソッドになります。
- そしてそれぞれのメソッドの key に対して、 `op` 型の object が value になります。

### op

- `op` は リクエストメソッドに対応する object で、以下の key を持ち得ます。
  - `summary`: リソースに対してどんな操作をするのか、簡潔に書きましょう。
  - `operationId`: この op を一意に特定する id です。 メソッド+リソース名が推奨です。
  - `parameters`: header, path, query など、場所に関わらずリクエストパラメータをここに書きます。
  - `requestBody`: post, put, patch のときに利用します。
  - `responses`: 200, 400 など、ステータスコードに対応する object を書きます。

## 演習

以下のような機能をもつ通販サイトを考えます。

- ユーザーがトップページにアクセスすると、購入可能な商品の一覧が表示される。
- 商品を選択して、カートに追加できる。
- カート内確認画面に遷移すると、カートに入った商品の一覧が表示される。

ここまでの機能を実装するために必要な API を洗い出して、仕様書を作成してください。
