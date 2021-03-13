import VueRouter from 'vue-router'
import Home from "@/components/pages/Home";
import LessonChat from "@/components/pages/LessonChat";

export default new VueRouter({
    routes:[
        {
            path: '/',
            component: Home
        },
        {
            path: '/:slug',
            component: LessonChat
        }
    ],
    mode: 'history'
})
