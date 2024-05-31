## API Guide

### Base URL

The base URL for all API endpoints is `/api/intake/`.

### Endpoints

#### IntakeForm

- Endpoint: `/api/intake/form/`
- Description: This endpoint is used to interact with the intake form data.

##### CRUD Operations

1. **Create (POST)**: `/api/intake/form/`
   - Required Parameters: `name`, `email`, `phone`, `campus_roll`, `department`, `batch`, `post`, `about`, `reason_to_join`, `interests`, `resume`
   - Optional Parameters: `github_link`, `linkedin_link`, `facebook_link`

2. **Read (GET)**: `/api/intake/form/` and `/api/intake/form/{id}/`
   - Required Parameters: None for `/api/form/`. For `/api/form/{id}/`, `id` is required.

3. **Update (PUT/PATCH)**: `/api/intake/form/{id}/`
   - Required Parameters: `id`
   - Optional Parameters: All other fields can be updated.

4. **Delete (DELETE)**: `/api/intake/form/{id}/`
   - Required Parameters: `id`
