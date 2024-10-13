package org.example;

import com.google.gson.Gson;
import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;

import java.io.*;
import java.nio.charset.StandardCharsets;
import java.util.logging.Level;
import java.util.logging.Logger;

public class HW7_lists {
    private static final Logger logger = Logger.getLogger(HW7_lists.class.getName());

    public static void main(String[] args) {
        String jsonData = readJsonFileFromResources("/spaces.json");

        JsonObject jsonObject = new Gson().fromJson(jsonData, JsonObject.class);
        processLists(jsonObject);
    }

    private static void processLists(JsonObject jsonObject) {
        JsonArray foldersArray = jsonObject.getAsJsonArray("folders");
        int totalListsFound = 0;
        int testListsFound = 0;

        System.out.println("\n======== Lists with names starting with 'test': ========");

        // Iterating through all folders and lists
        for (JsonElement folderElement : foldersArray) {
            JsonObject folder = folderElement.getAsJsonObject();
            JsonArray listsArray = folder.getAsJsonArray("lists");

            if (listsArray != null) {
                for (JsonElement listElement : listsArray) {
                    JsonObject list = listElement.getAsJsonObject();
                    totalListsFound++;

                    // If the list name starts with "test", output the space.name and space.id
                    if (list.has("name") && list.get("name").getAsString().toLowerCase().startsWith("test")) {
                        testListsFound++;
                        printListInfo(testListsFound, list);
                    }
                }
            }
        }

        System.out.println("\n======== Summary ========");
        System.out.println("Total lists found: " + totalListsFound);
        System.out.println("Lists with names starting with 'test': " + testListsFound);
    }

    private static void printListInfo(int index, JsonObject list) {
        System.out.println(index + ". List ID: " + list.get("id").getAsString());
        JsonObject space = list.getAsJsonObject("space");
        if (space != null) {
            System.out.println("Space Name: " + space.get("name").getAsString());
            System.out.println("Space ID: " + space.get("id").getAsString());
        }
    }

    // Method for reading a JSON file
    public static String readJsonFileFromResources(String fileName) {
        StringBuilder jsonData = new StringBuilder();
        try (InputStream inputStream = HW7_lists.class.getResourceAsStream(fileName)) {
            assert inputStream != null;
            try (BufferedReader reader = new BufferedReader(new InputStreamReader(inputStream, StandardCharsets.UTF_8))) {

                String line;
                while ((line = reader.readLine()) != null) {
                    jsonData.append(line);
                }
            }
        } catch (IOException e) {
            logger.log(Level.SEVERE, "Error reading file", e);
        }
        return jsonData.toString();
    }
}
