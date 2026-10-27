# Free job editor — setup guide

This version keeps GitHub Pages and the approved design. It adds a free hosted Pages CMS job editor.

## Upload
Upload **all** files and folders in this ZIP to the root of your existing GitHub repository, including hidden `.pages.yml` and `.github/workflows/build-jobs.yml`. GitHub's browser uploader can accept folders via drag-and-drop; verify hidden files appear in the repository afterwards. Keep the repository's default branch named `main`, or change the workflow's branch setting to match.

## Connect editor
1. Visit https://app.pagescms.org and sign in with GitHub.
2. Install/authorize the Pages CMS GitHub App for the Tir Chonaill Careers repository.
3. Open the repository in Pages CMS and select **Job vacancies**.
4. You should see Project Manager and Planner. Try editing the Planner summary and saving.
5. In GitHub, open **Actions** and check the `Publish job changes` workflow succeeded.
6. Refresh the live Jobs page after GitHub Pages has deployed.

## Let the client edit
Grant Shaun and Donal appropriate GitHub repository access, and have each sign into Pages CMS and authorize the app. They edit through Pages CMS, not GitHub's code editor. Because edits commit to the repository, give access only to trusted staff and enable two-factor authentication. This is **not** a completely separate admin account system.

## How jobs publish
Pages CMS saves a separate JSON file per job in `data/jobs/`. GitHub Actions automatically combines those files into `data/jobs-index.json`, which the website reads. To hide a job without deleting it, turn off `Show on website`.

## Important limitations
- This package does NOT create a private candidate dashboard or process CV uploads. The application form is still a demonstration; do not collect CVs until a secure service is connected.
- Pages CMS is a third-party hosted editor. Free availability and features may change.
- Job changes may take a few minutes to appear due to GitHub Actions and GitHub Pages deployments.
- If GitHub Actions does not have write permission, go to repository Settings > Actions > General > Workflow permissions and allow read/write (if available). Alternatively use a dedicated publishing workflow with a permitted token.
- Domain and email DNS remain unchanged.
