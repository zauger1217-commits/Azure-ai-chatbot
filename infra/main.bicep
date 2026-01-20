param appName string
param location string = resourceGroup().location

resource appServicePlan 'Microsoft.Web/serverfarms@2022-09-01' = {
  name: '${appName}-plan'
  location: location
  sku: {
    name: 'F1'
  }
}

resource webApp 'Microsoft.Web/sites@2022-09-01' = {
  name: appName
  location: location
  properties: {
    serverFarmId: appServicePlan.id
    siteConfig: {
      linuxFxVersion: 'PYTHON|3.11'
      appSettings: [
        { name: 'AZURE_OPENAI_ENDPOINT', value: 'REPLACE_ME' }
        { name: 'AZURE_OPENAI_KEY', value: 'REPLACE_ME' }
        { name: 'AZURE_OPENAI_DEPLOYMENT', value: 'gpt-4o-mini' }
      ]
    }
  }
}
