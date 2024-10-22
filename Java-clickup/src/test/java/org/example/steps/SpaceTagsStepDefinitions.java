package org.example.steps;

import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import io.restassured.response.Response;
import org.example.utils.RandomData;
import org.example.utils.ResourceUtils;
import org.json.JSONArray;
import org.json.JSONObject;
import org.junit.Assert;

public class SpaceTagsStepDefinitions extends BaseSteps {

    private final RandomData randomData = new RandomData();
    private String generatedTagName;
    private String updatedTagName;

    @When("I fetch space tags")
    public void fetchSpaceTags() {
        sharedTestData.setResponse(spaceTagsRestClient.getSpaceTags());
    }

    @When("I create a space tag with random name")
    public void createSpaceTag() {
        generatedTagName = "new_" + randomData.generateRandomString(6);
        sharedTestData.setResponse(spaceTagsRestClient.createSpaceTag(generatedTagName));
    }

    @When("Create a space tag form file {}")
    public void createSpaceTagFromFile(String path) {
        generatedTagName = "created_" + randomData.generateRandomString(6);
        String source = "data/folders/" + path;
        JSONObject body = ResourceUtils.readJson(source);
        JSONObject tagObject = body.getJSONObject("tag");
        tagObject.put("name", generatedTagName);
        Response response = spaceTagsRestClient.postSpaceTagFromFile(body.toString());
        sharedTestData.setResponse(response);
    }

    @When("I edit the space tag with random new name")
    public void editSpaceTag() {
        updatedTagName = "updated_" + randomData.generateRandomString(6);
        sharedTestData.setResponse(spaceTagsRestClient.editSpaceTag(generatedTagName, updatedTagName));
    }

    @When("I delete the space tag")
    public void deleteSpaceTag() {
        sharedTestData.setResponse(spaceTagsRestClient.deleteSpaceTag(generatedTagName));
    }

    @Then("the response should contain the created random tag for space")
    public void verifyResponseContainsRandomTag() {
        assertTagExists(generatedTagName, "Created tag was not found in the list of tags");
    }

    @Then("the response should contain the updated random tag for space")
    public void verifyResponseContainsUpdatedRandomTag() {
        assertTagExists(updatedTagName, "Updated tag was not found in the list of tags");
    }

    @Then("the response should not contain the deleted tag for space")
    public void verifyTagIsDeleted() {
        assertTagDoesNotExist(generatedTagName, "Deleted tag was found in the list of tags");
    }

    private void assertTagExists(String tagName, String errorMessage) {
        boolean tagFound = isTagInResponse(tagName);
        Assert.assertTrue(errorMessage, tagFound);
    }

    private void assertTagDoesNotExist(String tagName, String errorMessage) {
        boolean tagFound = isTagInResponse(tagName);
        Assert.assertFalse(errorMessage, tagFound);
    }

    private boolean isTagInResponse(String tagName) {
        String response = sharedTestData.getResponse().getBody().asString();
        if (!isResponseJson(response)) {
            throw new IllegalArgumentException("Response is not in JSON format.");
        }

        JSONObject obj = new JSONObject(response);
        JSONArray tagsArray = obj.getJSONArray("tags");

        for (int i = 0; i < tagsArray.length(); i++) {
            JSONObject tag = tagsArray.getJSONObject(i);
            if (tag.getString("name").equals(tagName)) {
                return true;
            }
        }
        return false;
    }

    private boolean isResponseJson(String response) {
        return response != null && !response.isEmpty() && response.trim().startsWith("{");
    }
}
