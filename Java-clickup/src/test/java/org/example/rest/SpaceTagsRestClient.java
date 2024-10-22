package org.example.rest;

import io.restassured.response.Response;

public class SpaceTagsRestClient extends BaseRestClient {

    private final String spaceId = "90121364847";
    private final String url = "/space/" + spaceId + "/tag/";

    public SpaceTagsRestClient() {
        this.setUpRestAssured();
    }

    public Response getSpaceTags2() {
        return this.requestSpec.get(url);
    }

    public Response getSpaceTags() {
        Response response = this.requestSpec
                .header("Authorization", "pk_2144410100_UHSIC7AK5SLLZTOD067P1TI0QIXO1YGD")
                .header("Content-Type", "application/json")
                .header("Accept", "application/json")
                .get(url);
        System.out.println("Response status code: " + response.getStatusCode());
        System.out.println("Response body: " + response.getBody().asString());

        return response;
    }

    public Response createSpaceTag2(String tagName) {
        String payload = "{ \"tag\": { \"name\": \"" + tagName + "\", \"tag_fg\": \"#000000\", \"tag_bg\": \"#000000\" } }";
        return this.requestSpec
                .body(payload)
                .post(url);
    }

    public Response postSpaceTagFromFile(String payload) {
        return this.requestSpec
                .body(payload)
                .post(url);
    }

    public Response createSpaceTag(String tagName) {
        String payload = "{ \"tag\": { \"name\": \"" + tagName + "\", \"tag_fg\": \"#000000\", \"tag_bg\": \"#000000\" } }";
        System.out.println("Creating tag with payload: " + payload);

        Response response = this.requestSpec
                .header("Authorization", "pk_2144410100_UHSIC7AK5SLLZTOD067P1TI0QIXO1YGD")
                .header("Content-Type", "application/json")
                .header("Accept", "application/json")
                .body(payload)
                .post(url);

        System.out.println("Response status code: " + response.getStatusCode());
        System.out.println("Response body: " + response.getBody().asString());

        return response;
    }


    public Response editSpaceTag(String oldTagName, String newTagName) {
        String payload = "{ \"tag\": { \"name\": \"" + newTagName + "\", \"tag_fg\": \"#000000\", \"tag_bg\": \"#000000\" } }";
        return this.requestSpec
                .body(payload)
                .put(url + oldTagName);
    }

    public Response deleteSpaceTag(String tagName) {
        return this.requestSpec.delete(url + tagName);
    }
}
