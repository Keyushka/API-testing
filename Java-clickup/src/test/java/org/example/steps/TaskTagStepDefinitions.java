package org.example.steps;

import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import org.example.utils.RandomData;
import org.json.JSONArray;
import org.json.JSONObject;

public class TaskTagStepDefinitions extends BaseSteps {

    private final RandomData randomData = new RandomData();
    private String generatedTagName;

    @When("I add tag with random name to task")
    public void addTagWithRandomNameToTask() {
        generatedTagName = "new_" + randomData.generateRandomString(8);
        sharedTestData.setResponse(taskTagRestClient.addTagToTask(generatedTagName));
    }

    @When("I remove tag with random name from task")
    public void removeTagWithRandomNameFromTask() {
        sharedTestData.setResponse(taskTagRestClient.removeTagFromTask(generatedTagName));
    }

    @When("I fetch task details")
    public void fetchTaskDetails() {
        sharedTestData.setResponse(taskTagRestClient.getTaskDetails());
    }

    @Then("the response should contain the random tag for task")
    public void verifyResponseContainsRandomTag() {
        assertTagExists(generatedTagName, "Created tag was not found in the task's tags");
    }

    @Then("the response should not contain the deleted tag for space random tag for task")
    public void verifyResponseDoesNotContainRandomTag() {
        assertTagNotExists(generatedTagName, "Deleted tag was still found in the task's tags");
    }

    private void assertTagExists(String tagName, String errorMessage) {
        String response = sharedTestData.getResponse().getBody().asString();
        JSONObject obj = new JSONObject(response);
        JSONArray tagsArray = obj.getJSONArray("tags");

        boolean tagFound = false;
        for (int i = 0; i < tagsArray.length(); i++) {
            JSONObject tag = tagsArray.getJSONObject(i);
            if (tag.getString("name").equals(tagName)) {
                tagFound = true;
                break;
            }
        }
        assert tagFound : errorMessage;
    }

    private void assertTagNotExists(String tagName, String errorMessage) {
        String response = sharedTestData.getResponse().getBody().asString();
        JSONObject obj = new JSONObject(response);
        JSONArray tagsArray = obj.getJSONArray("tags");

        boolean tagFound = false;
        for (int i = 0; i < tagsArray.length(); i++) {
            JSONObject tag = tagsArray.getJSONObject(i);
            if (tag.getString("name").equals(tagName)) {
                tagFound = true;
                break;
            }
        }
        assert !tagFound : errorMessage;
    }

}
