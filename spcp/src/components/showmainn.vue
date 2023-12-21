<template>
    <div class="box">
        <h1>{{ h1_text }}</h1>
        <div class="input-container">
            <input type="text" class="text" name="text" placeholder="请输入关键词..." required autofocus v-model="inputText"
                @keyup.enter="handleEnter">
            <button @click="generateText">生成</button>
            <el-textarea v-loading="loading" readonly :model="outputText" placeholder="梅花雪，梨花月，总相思。">{{ outputText
            }}</el-textarea>
        </div>
    </div>
</template>
  
<script>
import { ElLoading, } from 'element-plus'
import { ElMessage, ElMessageBox } from 'element-plus'
import Type from '../data/data';
export default {
    data() {
        return {
            h1_text: "情书生成器",
            inputText: "",
            outputText: "梅花雪，梨花月，总相思。",
            loading: false,
            type: Type//情书类型
        };
    },
    components: {
        ElLoading,
        ElMessage,
        ElMessageBox
    },
    created() {
        this.fetchH1Text();
    },

    methods: {
        fetchH1Text() {
            fetch("http://47.115.206.4:5000/get_h1_text")
                .then(response => response.json())
                .then(data => {
                    this.h1_text = data.h1_text;
                });
        },
        handleEnter(event) {  //按下回车或者点击时调用generateText将文本传入后端
            if (event.key === 'Enter') {
                this.generateText();
            }
        },
        generateText() {
            this.loading = true
            const input = this.inputText;
            fetch("http://47.115.206.4:5000/generate_text", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ input: input, type: this.type })
            })
                .then(response => response.json())
                .then(data => {
                    this.loading = false
                    this.outputText = data.generated_text;
                });
        }
    }
};

// module.exports = {
//   devServer: {
//     proxy: {
//       '/api': {
//         target: 'http://127.0.0.1:5000',
//         changeOrigin: true
//       }
//     }
//   }
// };
</script>
  
  
<style scoped>
.test {
    width: 400px;
    height: 400px;
    background-color: #95c0e6;
}

* {
    padding: 0;
    margin: 0;
}

.box {
    background-image: url("../assets/background.png");
    min-height: 100vh;
    width: 100%;
    background-size: cover;
}

h1,
h2,
h3,
h4,
h5,
h6,
p {
    margin: 0;
    padding: 0
}

.text1 {
    width: 100%;

}

h1 {
    text-align: center;
    line-height: 75px;
    color: #F5F5F5;
}

button,
input,
select {
    font-family: 'Noto Sans JP', sans-serif;
}

input {
    outline: none;
    margin-bottom: 15px;
    padding: 14px 20px;
    display: inline-block;
    box-sizing: border-box;
    border: none;
    outline: none;
    transition: .3s ease;
}

.iuput-box {
    display: flex;
}

el-textarea[readonly] {
    height: 400px;
    padding: 20px 20px;
    resize: none;
    overflow: auto;
    margin-bottom: 50px;
}

input,
el-textarea {
    width: 100%;
    display: block;
    font-size: 16px;
    text-align: center;
    background-color: #dfcade;
    opacity: 0.8;
    margin: 0 auto;
    border-radius: 10px;
    border: 1px solid #e5e5e5;
    color: #173f67;
}


button {
    opacity: 0.8;
    display: block;
    background-color: #95c0e6;
    border-radius: 10px;
    font-size: 16px;
    border: 1px solid #e5e5e5;
    padding: 14px 30px;
}


input {
    flex: 1;
}

button:active {
    opacity: 0.9;
    display: block;
    background-color: #95c0e6;
    border-radius: 10px;
    font-size: 16px;
    border: 1px solid #4c9deeef;
    padding: 14px 30px;
}

.input-container {
    width: 50%;
    margin: 0 auto;
    /* position: relative; */
    padding-top: 3%;
}

.input-container input[type="text"] {

    padding-right: 30px;
    /* 为 button 留出空间 */
    box-sizing: border-box;
    /* 让 padding 不增加元素的宽度 */
}

.input-container button {
    position: relative;
    top: -50px;
    right: -39px;
    /* 向右移动 39px */
    height: 100%;
    float: right;

}
</style>
  