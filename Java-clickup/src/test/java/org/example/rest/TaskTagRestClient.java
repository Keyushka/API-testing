package org.example.rest;

import io.restassured.response.Response;

public class TaskTagRestClient extends BaseRestClient {

    private final String taskId = "869630rqu";
    private final String teamId = "9012290639";
    private final String url = "/task/" + taskId + "/tag/";

    public TaskTagRestClient() {
        this.setUpRestAssured();
    }

    // Метод для додавання тегу до задачі (тіло запиту не передається)
    public Response addTagToTask(String tagName) {
        return this.requestSpec
                .queryParam("custom_task_ids", true)
                .queryParam("team_id", teamId)
                .post(url + tagName);
    }

    // Метод для видалення тегу з задачі (тіло запиту не передається)
    public Response removeTagFromTask(String tagName) {
        return this.requestSpec
                .queryParam("custom_task_ids", true)
                .queryParam("team_id", teamId)
                .delete(url + tagName);
    }

    // Метод для отримання всієї інформації про задачу, включаючи теги
    public Response getTaskDetails() {
        return this.requestSpec
                .queryParam("custom_task_ids", true)
                .queryParam("team_id", teamId)
                .get("/task/" + taskId);
    }
}
