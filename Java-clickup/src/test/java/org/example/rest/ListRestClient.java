package org.example.rest;

import io.restassured.response.Response;

public class ListRestClient extends BaseRestClient{
    String listUrl = "folder/90122619398/list";

    public ListRestClient(){
        this.setUpRestAssured();
    }

    public Response getLists(){
        return this.requestSpec.get(listUrl);
    }

}