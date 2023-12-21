//主页面
<template>
    <div class="containor">
        <div class="title">
            <h1>LoveStory</h1>
            <button @click="dialogVisible = true">让爱从这里开始(点击获得专属情书)</button>
            <el-dialog v-model="dialogVisible" title="分类" width="30%">
                <el-radio-group>
                    <Son v-for="item in items" key="item.id" @click="select(item.id)">{{ item.name }}</Son>
                    <!-- <el-button class="search" @click="toMain">Search</el-button> -->
                </el-radio-group>
            </el-dialog>
        </div>
    </div>
</template>

<style scoped>
* {
    margin: 0;
    padding: 0;
}

.el-radio-group {
    display: flex;
    justify-content: space-around;
}

el-button {
    position: relative;
    right: 180px;
}

.title h1 {
    color: aliceblue;
    font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
    font-size: 150px;
}

el-button {
    border: 1px solid;
}

button {
    background: none;
    border: none;
    /* border: 1px solid rgba(25, 120, 221, 0.5) ; */
}

.title h3 {
    color: aliceblue;
    font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
}

.containor {
    background: url("../assets/images/banner/banner2.jpg") no-repeat center center;
    min-height: 100vh;
    width: 100%;
    background-size: cover;
    position: relative;
    display: flex;

}

.title {
    width: 100%;
    height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}

.search {
    margin-left: 30px;
}
</style>

<script setup>
import { ref } from 'vue'
import router from '../router/router';
import Son from '../components/searchItem.vue'
import axios from 'axios';

const dialogVisible = ref(false)
const items = ref(
    [{
        id: 1,
        name: "文艺"
    },
    {
        id: 2,
        name: "悬疑"
    },
    {
        id: 3,
        name: "惊悚"
    },
    {
        id: 4,
        name: "浪漫"
    }
    
    ])
console.log(items.value[2]);
const toMain = (i) => {
    router.push({
        path: "/qingshu",
    })
    console.log(i)
}
const select = (i) => {
    toMain(i)

    const data = { id: i }; // 创建包含 id 属性的对象
    axios.post('http://47.115.206.4:5000/getMsg', data, {
      headers: {
        'Content-Type': 'application/json'
      }
    })
    .then(response => {
      // 请求成功后的处理
    })
    .catch(error => {
      // 请求失败后的处理
    });

}

const getType = () => {
    axios({
        url: "",
        method: "GET"
    }).then(res => {
        items = res.data
    })
}
</script>