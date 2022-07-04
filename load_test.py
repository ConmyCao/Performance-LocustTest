from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    host = "https://baike.baidu.com"  # 配置URL
    wait_time = between(1, 2)
    # wait_time = constant(3)  # 每次请求停顿时间 （思考时间）
    # 每个模拟用户开始执行，只执行一次
    # def on_start(self):
    #     self.client.post("/login", json={"username":"foo", "password":"bar"})

    @task
    def hello_world(self):
        self.client.get("/item/鹿鸣文苑/18780244?fr=aladdin")
        self.client.get("/world")
    # task()参数用于指定该行为的执行权重。参数越大每次被虚拟用户执行的概率越高。
    # @task(3)
    # def view_item(self):
    #     for item_id in range(10):
    #         self.client.get(f"/item?id={item_id}", name="/item")

    # CMD: locust -f load_test.py
