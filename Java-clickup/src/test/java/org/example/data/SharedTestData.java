package org.example.data;

import io.restassured.response.Response;

public class SharedTestData {
    private Response response;
    private String responseBody;


    public Response getResponse() {
        return response;
    }

    public void setResponse(Response response) {
        this.response = response;
    }

    public String getResponseBody() {
        return responseBody;
    }

    public void setResponseBody(String responseBody) {
        this.responseBody = responseBody;
    }





}