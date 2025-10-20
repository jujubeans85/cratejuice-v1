# GitHub Actions Workflows

## create-deploy.yml

This workflow creates a GitHub deployment and deploys the project to AWS S3.

### Workflow Overview

The workflow performs the following steps:
1. Creates a GitHub deployment via the Deployments API
2. Sets deployment status to `in_progress`
3. Installs dependencies (if `package.json` exists)
4. Runs tests (if test scripts are configured)
5. Builds the project (runs `npm run build` or prepares static files)
6. Uploads the `build/` directory to S3 using `aws s3 sync`
7. Optionally invalidates CloudFront cache (when `CLOUDFRONT_DISTRIBUTION_ID` is set)
8. Sets deployment status to `success` on workflow success, or `failure` on error

### Triggers

- Push to `main` branch
- Manual workflow dispatch

### Required Secrets

Configure the following secrets in your repository settings:

- `AWS_ACCESS_KEY_ID` - AWS access key ID for authentication
- `AWS_SECRET_ACCESS_KEY` - AWS secret access key for authentication
- `AWS_REGION` - AWS region where your S3 bucket is located (e.g., `us-east-1`)
- `S3_BUCKET` - Name of the S3 bucket to deploy to

### Optional Secrets

- `CLOUDFRONT_DISTRIBUTION_ID` - CloudFront distribution ID for cache invalidation (optional)

### Notes

- The workflow uses `npm test` and `npm run build` if a `package.json` file is present
- If your project uses different package managers (yarn, pnpm) or different output directories (dist/, public/), update the workflow accordingly
- The `required_contexts` parameter in the deployment creation is set to an empty array; add required status checks there if you want to block deployments until checks pass
- Static files are copied to the `build/` directory if no build script is found

### Customization

For projects with different configurations:
- **Different package manager**: Replace `npm` with `yarn` or `pnpm` commands
- **Different build output**: Change `build/` to your output directory (e.g., `dist/`, `public/`)
- **Additional build steps**: Add steps between "Build project" and "Configure AWS credentials"
