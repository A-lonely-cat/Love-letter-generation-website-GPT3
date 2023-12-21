from flask import Flask, jsonify, request, render_template
import sql
import chatGpt3


# 指定静态文件
app = Flask(__name__,
            template_folder="./dist",
            static_folder="./dist",
            static_url_path="")

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
@app.route("/")
def index():
    return render_template("index.html")


type_item = {1:"文艺" , 2:"悬疑", 3: "惊悚", 4: "浪漫", 5: "", 6: "", 7: ""}
wordType = []

@app.route('/get_h1_text', methods=['GET'])
def get_h1_text():
    if(sql.redom_select()):
        h1_text = sql.redom_select()        # 随机读取数据库内容
    else:
        h1_text = "人生之若初见"
    return jsonify({'h1_text': h1_text})


@app.route("/getMsg", methods=["post"])
def qingshu():
    id=request.json.get("id")
    word_type = type_item[id]
    wordType.clear()
    wordType.append(word_type)
    return "Success"


@app.route("/generate_text", methods=["POST"])
def generate_text():
    # 获取输入框数据即关键词
    input_text = request.json.get("input")
    # chatGpt3处理数据并返回结果

    python_variable_text = chatGpt3.chat_gpt3(wordType[0],input_text)
    return jsonify({'generated_text': python_variable_text})



if __name__ == "__main__":
    app.run()