import axios from "axios";

// 创建一个新的axios对象
const request = axios.create({
    baseURL: "http://yangxiao666.natapp1.cc",
    timeout: 30000
})

export default request;