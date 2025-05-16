[![DOI](https://zenodo.org/badge/984867587.svg)](https://doi.org/10.5281/zenodo.15446418)

# zenodo-github_integration_template

## Overview
This repository provides a template for integrating Zenodo with GitHub. It includes features such as file naming convention checks and Zenodo JSON validation to ensure proper metadata formatting for Zenodo uploads.

## Features
- **Zenodo JSON Validation**: Ensures that the `.zenodo.json` file adheres to the required schema for Zenodo metadata.
- **File Naming Convention Check**: Verifies that files in the repository follow a predefined naming convention.
- **CC-BY-4.0 License**: The repository is licensed under the Creative Commons Attribution 4.0 International License.

## Repository Structure
- **`.zenodo.json`**: Metadata file for Zenodo integration. This file includes information such as the dataset title, creators, description, license, and keywords.
- **`README.md`**: Documentation for the repository.
- **`LICENSE`**: Contains the full text of the CC-BY-4.0 license.
- **Other Files**: Additional files related to the dataset or project.

## Proper Usage

To trigger this workflow, follow these steps:

### Push Changes
- Make changes to the specified files or directories (e.g., `data/**`) in the `main` branch.
- Push the changes to the repository. The workflow will automatically run.

### Create a Pull Request
- Create a new branch and make changes to the specified files or directories (e.g., `data/**`).
- Open a pull request targeting the `main` branch. The workflow will run automatically when the pull request is opened, updated, or synchronized.

## Benefits of This Configuration
- **Selective Triggering**: The workflow only runs when relevant files are modified, optimizing resource usage.
- **Code Review Integration**: By using pull requests, you can ensure that changes are reviewed and tested before being merged into the `main` branch.
- **Automation**: Automates repetitive tasks, such as validation or testing, ensuring consistency and reducing manual effort.

## How to Use The Zenodo JSON
1. **Update `.zenodo.json`**:
   - Add your dataset metadata, including title, creators, description, and license.
   - Example:
     ```json
     {
       "upload_type": "dataset",
       "title": "Your Dataset Title",
       "creators": [
         {
           "name": "Your Name",
           "affiliation": "Your Organization",
           "orcid": "Your ORCID"
         }
       ],
       "description": "A brief description of your dataset.",
       "access_right": "open",
       "license": "CC-BY-4.0",
       "keywords": ["example", "zenodo", "github"]
     }
     ```

2. **Validate `.zenodo.json`**:
   - Use a JSON schema validator to ensure the file is correctly formatted.

3. **Check File Naming Conventions**:
   - Ensure all files follow the required naming conventions for your project.

4. **Publish to Zenodo**:
   - Once the repository is ready, push it to GitHub. Zenodo will automatically create a DOI for the release if integration is enabled.
## GitHub Actions
This repository can include GitHub Actions workflows to automate tasks such as validating the `.zenodo.json` file or ensuring file naming conventions are followed. Example workflows might include:
- **JSON Validation**: A workflow that runs a JSON schema validator on `.zenodo.json` to ensure it adheres to the required format.
- **Linting and Testing**: A workflow that checks for code quality and runs tests.

## Setting Up Zenodo-GitHub Connection

To integrate Zenodo with GitHub and enable automatic DOI generation for your repository releases, follow these detailed steps:

### 1. **Link Your GitHub Account to Zenodo**
   - Log in to Zenodo at [https://zenodo.org/](https://zenodo.org/) (or [https://sandbox.zenodo.org/](https://sandbox.zenodo.org/) for testing).
   - Navigate to **Account Settings** by clicking your profile picture in the top-right corner.
   - Under **Applications**, go to the **GitHub** tab and click **Connect**.
   - Authorize Zenodo to access your GitHub account. This allows Zenodo to monitor your repositories and create DOIs for releases.

### 2. **Enable Zenodo Integration for Your Repository**
   - In Zenodo, go to the **GitHub** tab under **Account Settings**.
   - Locate the repository you want to integrate and toggle the switch to enable Zenodo integration.
   - Zenodo will now monitor this repository for new releases.

### 3. **Prepare Your Repository**
   - Add a `.zenodo.json` file to your repository with the required metadata. Example:
     ```json
     {
       "upload_type": "dataset",
       "title": "Example Dataset for Zenodo Sandbox Publishing",
       "creators": [
         {
           "name": "Martin Schätz",
           "affiliation": "UCT Prague",
           "orcid": "0000-0003-0931-4017"
         }
       ],
       "description": "<p>This is an example dataset published to the Zenodo Sandbox via GitHub integration.</p>",
       "access_right": "open",
       "license": "CC-BY-4.0",
       "keywords": [
         "example",
         "zenodo",
         "github",
         "sandbox"
       ]
     }
     ```
   - Validate the `.zenodo.json` file using a JSON schema validator to ensure it is correctly formatted.

### 4. **Create a Release in GitHub**
   - Go to your repository on GitHub.
   - Click the **Releases** tab and then **Draft a new release**.
   - Fill in the release details:
     - **Tag version**: Specify a version number (e.g., `v1.0.0`).
     - **Release title**: Provide a title for the release.
     - **Description**: Add a description of the release.
   - Attach any relevant files (e.g., datasets or documentation) if needed.
   - Click **Publish release**.

### 5. **Zenodo Processes the Release**
   - Zenodo will automatically archive the release and generate a DOI.
   - You can view the DOI in your Zenodo account under the **Uploads** section.

### 6. **Verify and Add the DOI**
   - Check the DOI generated by Zenodo to ensure it is correct.
   - Add the DOI badge to your repository's `README.md` file for visibility. Example:
     ```markdown
     [![DOI](https://zenodo.org/badge/DOI/10.1234/example.svg)](https://doi.org/10.1234/example)
     ```

### Notes
- Use [Zenodo Sandbox](https://sandbox.zenodo.org/) for testing purposes. DOIs generated in the sandbox are not valid for production.
- Ensure the `.zenodo.json` file is updated before creating a release, as Zenodo uses it to populate metadata for the DOI.

### Example `.zenodo.json` for a restricted access deposit:**

```json
{
  "upload_type": "dataset",
  "title": "Example Restricted Dataset from GitHub",
  "creators": [
    {
      "name": "Your Organization Name",
      "affiliation": "Your Organization"
    }
  ],
  "description": "<p>This is an example dataset published to Zenodo with restricted access initially.</p>",
  "access_right": "restricted",
  "license": "CC-BY-4.0",
  "keywords": [
    "example",
    "zenodo",
    "github",
    "restricted"
  ],
  "communities": [
    {
      "id": "zenodo-sandbox"
    }
  ]
}
```
for a closed access deposit:
```json
{
  "upload_type": "dataset",
  "title": "Example Closed Dataset from GitHub",
  "creators": [
    {
      "name": "Your Organization Name",
      "affiliation": "Your Organization"
    }
  ],
  "description": "<p>This is an example dataset published to Zenodo with closed access initially.</p>",
  "access_right": "closed",
  "license": "CC-BY-4.0",
  "keywords": [
    "example",
    "zenodo",
    "github",
    "closed"
  ],
  "communities": [
    {
      "id": "zenodo-sandbox"
    }
  ]
}
```
for an embargoed access deposit:
```json
{
  "upload_type": "dataset",
  "title": "Example Embargoed Dataset from GitHub",
  "creators": [
    {
      "name": "Your Organization Name",
      "affiliation": "Your Organization"
    }
  ],
  "description": "<p>This is an example dataset published to Zenodo with an embargo.</p>",
  "access_right": "embargoed",
  "embargo_date": "2026-01-01",
  "license": "CC-BY-4.0",
  "keywords": [
    "example",
    "zenodo",
    "github",
    "embargo"
  ],
  "communities": [
    {
      "id": "zenodo-sandbox"
    }
  ]
}
```


## License
This repository is licensed under the Creative Commons Attribution 4.0 International License (CC-BY-4.0). For more details, see the `LICENSE` file or visit [https://creativecommons.org/licenses/by/4.0/](https://creativecommons.org/licenses/by/4.0/).

## Contributing
Contributions are welcome! Please ensure that your changes adhere to the repository's guidelines and include proper documentation.

## Contact
For questions or support, please contact the repository maintainer.
