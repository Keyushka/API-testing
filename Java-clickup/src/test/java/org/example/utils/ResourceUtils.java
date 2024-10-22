package org.example.utils;

import lombok.SneakyThrows;
import org.example.steps.BaseSteps;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.URL;

public abstract class ResourceUtils {
    private ResourceUtils() {
    }

    @SneakyThrows
    public static JSONObject readJson(String resourcePath) {
        URL resourceUrl = BaseSteps.class.getClassLoader().getResource(resourcePath);
        if (resourceUrl == null) {
            throw new IllegalArgumentException("Resource not found: " + resourcePath);
        }

        try (InputStream inputStream = resourceUrl.openStream();
             BufferedReader reader = new BufferedReader(new InputStreamReader(inputStream))) {
            StringBuilder jsonString = new StringBuilder();
            String line;
            while ((line = reader.readLine()) != null) {
                jsonString.append(line);
            }
            return new JSONObject(jsonString.toString());
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    @SneakyThrows
    public static InputStream getFile(String resourcePath) {
        URL resourceUrl = BaseSteps.class.getClassLoader().getResource(resourcePath);
        if (resourceUrl != null) {
            try {
                return resourceUrl.openStream();
            } catch (Exception e) {
                e.printStackTrace();
            }
        } else {
            System.out.println("Resource not found: " + resourcePath);
        }
        return null;
    }

}