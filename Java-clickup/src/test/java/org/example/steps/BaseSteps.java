package org.example.steps;

import org.example.data.SharedTestData;
import org.example.rest.FoldersRestClient;
import org.example.rest.ListRestClient;
import org.example.rest.SpaceTagsRestClient;
import org.example.rest.TaskTagRestClient;

public class BaseSteps {

    protected FoldersRestClient foldersRestClient = new FoldersRestClient();
    protected ListRestClient listRestClient = new ListRestClient();
    protected SpaceTagsRestClient spaceTagsRestClient = new SpaceTagsRestClient();
    protected TaskTagRestClient taskTagRestClient = new TaskTagRestClient();
    protected static SharedTestData sharedTestData = new SharedTestData();
}
