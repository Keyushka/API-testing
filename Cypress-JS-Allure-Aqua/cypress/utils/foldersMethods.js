import {faker} from "@faker-js/faker";

const foldersURL = '/space/90121364847/folder'

export const getFolders = ()=>{
    return cy.sentRequest('GET', foldersURL, null)
}

export const createFolder = ()=>{
    const body = {name: faker.internet.userName()}
    return cy.sentRequest('POST', foldersURL, body)
}

export const updateFolder = (id)=>{
    const newBody = {name: faker.internet.userName()}
    return cy.sentRequest('PUT', `/folder/${id}`, newBody)
}

export const deleteFolder = (id)=>{
    return cy.sentRequest('DELETE', `/folder/${id}`, null)
}