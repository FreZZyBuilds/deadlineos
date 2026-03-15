# TestSprite AI Testing Report (MCP)

## 1️⃣ Document Metadata
- **Project Name:** deadlineos
- **Date:** 2026-03-15
- **Prepared by:** TestSprite AI Team (via MCP) + Trae IDE assistant
- **Test Scope:** Frontend (codebase)
- **Base URL:** http://localhost:5173/
- **Server Mode:** Production-like static server (http-server)

## 2️⃣ Requirement Validation Summary
### Requirement: Site Navigation
#### Test TC001 — Navigate from landing page to Features via header navigation
- **Test Code:** [TC001_Navigate_from_landing_page_to_Features_via_header_navigation.py](./testsprite_tests/TC001_Navigate_from_landing_page_to_Features_via_header_navigation.py)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/bef31d81-f209-40d5-9c3b-2ae12f2864d1/c55d0984-0b84-4478-8cab-4b158548df85
- **Status:** ✅ Passed
- **Analysis / Findings:** Header navigation is visible and routes correctly to `/dos-features.html`.

#### Test TC002 — Navigate from landing page to Pricing via header navigation
- **Test Code:** [TC002_Navigate_from_landing_page_to_Pricing_via_header_navigation.py](./testsprite_tests/TC002_Navigate_from_landing_page_to_Pricing_via_header_navigation.py)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/bef31d81-f209-40d5-9c3b-2ae12f2864d1/7d8fb158-68ed-4d51-9955-858e427587d6
- **Status:** ✅ Passed
- **Analysis / Findings:** Header navigation routes correctly to `/dos-pricing.html`.

#### Test TC003 — Navigate from landing page to Demo via header navigation
- **Test Code:** [TC003_Navigate_from_landing_page_to_Demo_via_header_navigation.py](./testsprite_tests/TC003_Navigate_from_landing_page_to_Demo_via_header_navigation.py)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/bef31d81-f209-40d5-9c3b-2ae12f2864d1/02f3932b-aac2-4b9a-8ec9-8bfa9358b5c3
- **Status:** ✅ Passed
- **Analysis / Findings:** Header navigation routes correctly to `/dos-demo.html`.

#### Test TC004 — Launch the in-browser app from the Demo page using Open App/Launch App
- **Test Code:** [TC004_Launch_the_in_browser_app_from_the_Demo_page_using_Open_AppLaunch_App.py](./testsprite_tests/TC004_Launch_the_in_browser_app_from_the_Demo_page_using_Open_AppLaunch_App.py)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/bef31d81-f209-40d5-9c3b-2ae12f2864d1/9eb300ed-ff8a-4bda-9e93-a4535b494f9a
- **Status:** ✅ Passed
- **Analysis / Findings:** The app entry point works and `/deadlineos-v3.html` loads successfully.

#### Test TC005 — Handle missing page navigation by showing the 404 page
- **Test Code:** [TC005_Handle_missing_page_navigation_by_showing_the_404_page.py](./testsprite_tests/TC005_Handle_missing_page_navigation_by_showing_the_404_page.py)
- **Status:** ❌ Failed
- **Analysis / Findings:** This test expects Compare/Pitch links to route to `/404.html`, but other navigation tests validate Compare/Pitch as valid pages. Treat as a test expectation conflict (needs test update).

#### Test TC006 — Navigate from landing page to Roadmap via header navigation
- **Test Code:** [TC006_Navigate_from_landing_page_to_Roadmap_via_header_navigation.py](./testsprite_tests/TC006_Navigate_from_landing_page_to_Roadmap_via_header_navigation.py)
- **Status:** ✅ Passed
- **Analysis / Findings:** Header navigation routes correctly to `/dos-roadmap.html`.

#### Test TC007 — Navigate from landing page to Compare via header navigation
- **Test Code:** [TC007_Navigate_from_landing_page_to_Compare_via_header_navigation.py](./testsprite_tests/TC007_Navigate_from_landing_page_to_Compare_via_header_navigation.py)
- **Status:** ✅ Passed
- **Analysis / Findings:** Header navigation routes correctly to `/dos-compare.html`.

#### Test TC008 — Navigate from landing page to Pitch via header navigation
- **Test Code:** [TC008_Navigate_from_landing_page_to_Pitch_via_header_navigation.py](./testsprite_tests/TC008_Navigate_from_landing_page_to_Pitch_via_header_navigation.py)
- **Status:** ✅ Passed
- **Analysis / Findings:** Header navigation routes correctly to `/pitch.html`.

### Requirement: Local Profile Login
#### Test TC009 — Create a new PIN-protected profile and log in successfully
- **Test Code:** [TC009_Create_a_new_PIN_protected_profile_and_log_in_successfully.py](./testsprite_tests/TC009_Create_a_new_PIN_protected_profile_and_log_in_successfully.py)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/ea8fd31b-d93e-40da-ad45-107771fa04f9/df68d480-acda-44af-b38d-e133898f7955
- **Status:** ✅ Passed
- **Analysis / Findings:** Profile creation + PIN login works end-to-end and closes the login overlay.

#### Test TC010 — Validation: profile name is required
- **Test Code:** [TC010_Validation_profile_name_is_required.py](./testsprite_tests/TC010_Validation_profile_name_is_required.py)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/ea8fd31b-d93e-40da-ad45-107771fa04f9/61d2a21d-f7e1-435e-ab0b-961873d83568
- **Status:** ✅ Passed
- **Analysis / Findings:** Create-profile flow shows a visible “required” validation error when name is empty.

### Requirement: Task Management
#### Test TC012 — Prevent adding a task when title is empty
- **Test Code:** [TC012_Prevent_adding_a_task_when_title_is_empty.py](./testsprite_tests/TC012_Prevent_adding_a_task_when_title_is_empty.py)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/ea8fd31b-d93e-40da-ad45-107771fa04f9/dc69399f-ee38-4429-88dd-deab69005875
- **Status:** ✅ Passed
- **Analysis / Findings:** Submitting an empty task shows a visible inline validation message and blocks creation.

#### Test TC013 — Persist tasks to localStorage after page reload
- **Test Code:** [TC013_Persist_tasks_to_localStorage_after_page_reload.py](./testsprite_tests/TC013_Persist_tasks_to_localStorage_after_page_reload.py)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/06322027-2c22-43a8-a339-0d00432c965c/bb0848b9-53bd-4a8f-9cce-2ad9adc71a93
- **Status:** ✅ Passed
- **Analysis / Findings:** A created task remains present after a full page reload, confirming localStorage persistence.

#### Test TC011 — Create a task with deadline and priority, then edit priority, complete, and delete it
- **Test Code:** [TC011_Create_a_task_with_deadline_and_priority_then_edit_priority_complete_and_delete_it.py](./testsprite_tests/TC011_Create_a_task_with_deadline_and_priority_then_edit_priority_complete_and_delete_it.py)
- **Status:** ❌ Failed
- **Analysis / Findings:** Generated test script is incomplete/contradictory (does not perform the planned actions and includes conflicting assertions). Requires test case correction in the dashboard.

#### Test TC014 — Cancel deletion leaves the task intact
- **Test Code:** [TC014_Cancel_deletion_leaves_the_task_intact.py](./testsprite_tests/TC014_Cancel_deletion_leaves_the_task_intact.py)
- **Status:** ✅ Passed
- **Analysis / Findings:** Deletion confirmation modal Cancel keeps the task visible.

#### Test TC015 — Deadline countdown appears for tasks with deadlines
- **Test Code:** [TC015_Deadline_countdown_appears_for_tasks_with_deadlines.py](./testsprite_tests/TC015_Deadline_countdown_appears_for_tasks_with_deadlines.py)
- **Status:** ✅ Passed
- **Analysis / Findings:** Tasks with a deadline display a countdown indicator.

#### Test TC016 — Change priority on an existing task and verify it persists after reload
- **Test Code:** [TC016_Change_priority_on_an_existing_task_and_verify_it_persists_after_reload.py](./testsprite_tests/TC016_Change_priority_on_an_existing_task_and_verify_it_persists_after_reload.py)
- **Status:** ✅ Passed
- **Analysis / Findings:** Priority changes persist across a full page reload.

#### Test TC017 — Delete a task and verify it stays deleted after reload
- **Test Code:** [TC017_Delete_a_task_and_verify_it_stays_deleted_after_reload.py](./testsprite_tests/TC017_Delete_a_task_and_verify_it_stays_deleted_after_reload.py)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/06322027-2c22-43a8-a339-0d00432c965c/13664369-b442-4506-a15c-7ef0a62b5c7a
- **Status:** ✅ Passed
- **Analysis / Findings:** Deleted tasks remain deleted after reload (no reappearance from persistence layer).

### Requirement: AI Commander (Chat/Analyze/Autoprioritize)
#### Test TC018 — Analyze in Demo mode shows AI analysis output
- **Test Code:** [TC018_Analyze_in_Demo_mode_shows_AI_analysis_output.py](./testsprite_tests/TC018_Analyze_in_Demo_mode_shows_AI_analysis_output.py)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/06322027-2c22-43a8-a339-0d00432c965c/e02d0dbb-d28a-4687-b5db-527e13b55277
- **Status:** ✅ Passed
- **Analysis / Findings:** Analyze updates the AI output area with a response (mock/fallback path accepted).

#### Test TC019 — AI Chat: send a message and receive an assistant reply
- **Test Code:** [TC019_AI_Chat_send_a_message_and_receive_an_assistant_reply.py](./testsprite_tests/TC019_AI_Chat_send_a_message_and_receive_an_assistant_reply.py)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/06322027-2c22-43a8-a339-0d00432c965c/77d8fa42-a2a8-47ef-aaca-2a6cca58e65d
- **Status:** ✅ Passed
- **Analysis / Findings:** Chat flow renders a user message and then an AI assistant reply.

#### Test TC020 — API key overlay: switching tabs retains expected UI elements
- **Test Code:** [TC020_API_key_overlay_switching_tabs_retains_expected_UI_elements.py](./testsprite_tests/TC020_API_key_overlay_switching_tabs_retains_expected_UI_elements.py)
- **Status:** ✅ Passed
- **Analysis / Findings:** Demo/Own Key tabs keep the expected UI visible (input and demo counter).

#### Test TC021 — Analyze with invalid API key shows fallback response or visible error
- **Test Code:** [TC021_Analyze_with_invalid_API_key_shows_fallback_response_or_visible_error.py](./testsprite_tests/TC021_Analyze_with_invalid_API_key_shows_fallback_response_or_visible_error.py)
- **Status:** ✅ Passed
- **Analysis / Findings:** Invalid key produces a visible error in the AI output (or acceptable fallback behavior).

#### Test TC022 — Auto-Prioritize in Demo mode produces visible AI suggestions
- **Test Code:** [TC022_Auto_Prioritize_in_Demo_mode_produces_visible_AI_suggestions.py](./testsprite_tests/TC022_Auto_Prioritize_in_Demo_mode_produces_visible_AI_suggestions.py)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/391e9166-5bbd-4108-9087-7cf1ec3a273c/f664c22c-7933-45df-af57-14f6574ab437
- **Status:** ✅ Passed
- **Analysis / Findings:** Auto-Prioritize produces a visible prioritized output and updates task scoring (fallback scoring accepted).

#### Test TC023 — AI Chat: empty message is blocked with visible validation
- **Test Code:** [TC023_AI_Chat_empty_message_is_blocked_with_visible_validation.py](./testsprite_tests/TC023_AI_Chat_empty_message_is_blocked_with_visible_validation.py)
- **Status:** ✅ Passed
- **Analysis / Findings:** Empty chat submit is blocked and shows a validation message.

#### Test TC024 — AI Chat: multiple consecutive messages maintain ordered history
- **Test Code:** [TC024_AI_Chat_multiple_consecutive_messages_maintain_ordered_history.py](./testsprite_tests/TC024_AI_Chat_multiple_consecutive_messages_maintain_ordered_history.py)
- **Status:** ✅ Passed
- **Analysis / Findings:** Consecutive messages preserve ordering in chat history.

#### Test TC025 — Closing AI overlay does not block subsequent AI actions
- **Test Code:** [TC025_Closing_AI_overlay_does_not_block_subsequent_AI_actions.py](./testsprite_tests/TC025_Closing_AI_overlay_does_not_block_subsequent_AI_actions.py)
- **Status:** ✅ Passed
- **Analysis / Findings:** Returning from Chat does not prevent Analyze/Auto-Prioritize from working.

### Requirement: Focus Timer
#### Test TC026 — Complete a focus session and see it reflected in local stats and analytics
- **Test Code:** [TC026_Complete_a_focus_session_and_see_it_reflected_in_local_stats_and_analytics.py](./testsprite_tests/TC026_Complete_a_focus_session_and_see_it_reflected_in_local_stats_and_analytics.py)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/11f485d2-41a7-43aa-b419-63761cbb8976/12e0ef57-71cf-4b94-a5f7-c4d867567f7b
- **Status:** ✅ Passed
- **Analysis / Findings:** Completing a session and saving it updates focus stats and analytics.

#### Test TC027 — Reset an active timer and confirm no session is added
- **Test Code:** [TC027_Reset_an_active_timer_and_confirm_no_session_is_added.py](./testsprite_tests/TC027_Reset_an_active_timer_and_confirm_no_session_is_added.py)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/11f485d2-41a7-43aa-b419-63761cbb8976/99381853-77eb-4892-81c7-a185386c6c64
- **Status:** ✅ Passed
- **Analysis / Findings:** Reset cancels the running timer without incrementing session stats.

#### Test TC028 — Prevent starting the timer twice while it is already running
- **Test Code:** [TC028_Prevent_starting_the_timer_twice_while_it_is_already_running.py](./testsprite_tests/TC028_Prevent_starting_the_timer_twice_while_it_is_already_running.py)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/11f485d2-41a7-43aa-b419-63761cbb8976/21a27219-5b41-4577-9366-5be0c9668cbb
- **Status:** ✅ Passed
- **Analysis / Findings:** Starting while already running is prevented and provides user feedback; Stop remains available.

#### Test TC031 — Session stats increase after saving a session
- **Test Code:** [TC031_Session_stats_increase_after_saving_a_session.py](./testsprite_tests/TC031_Session_stats_increase_after_saving_a_session.py)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/11f485d2-41a7-43aa-b419-63761cbb8976/f748d8ff-0d04-4295-8625-d99958197221
- **Status:** ✅ Passed
- **Analysis / Findings:** Save Session increments stored focus minutes and session counters.

#### Test TC029 — Stop a running timer and confirm it is no longer running
- **Test Code:** [TC029_Stop_a_running_timer_and_confirm_it_is_no_longer_running.py](./testsprite_tests/TC029_Stop_a_running_timer_and_confirm_it_is_no_longer_running.py)
- **Status:** ❌ Failed
- **Analysis / Findings:** Generated test contains conflicting assertions (expects Stop visible and not visible) and brittle selectors; requires test case correction in the dashboard.

#### Test TC030 — Save Session appears only after stopping/ending a run (if the app prompts)
- **Test Code:** [TC030_Save_Session_appears_only_after_stoppingending_a_run_if_the_app_prompts.py](./testsprite_tests/TC030_Save_Session_appears_only_after_stoppingending_a_run_if_the_app_prompts.py)
- **Status:** ❌ Failed
- **Analysis / Findings:** Generated test contains conflicting assertions (expects Save Session not visible and visible); requires test case correction in the dashboard.

#### Test TC032 — Reset after stopping does not create a session and returns timer to initial value
- **Test Code:** [TC032_Reset_after_stopping_does_not_create_a_session_and_returns_timer_to_initial_value.py](./testsprite_tests/TC032_Reset_after_stopping_does_not_create_a_session_and_returns_timer_to_initial_value.py)
- **Status:** ✅ Passed
- **Analysis / Findings:** Reset after stop returns timer state and does not increment sessions.

### Requirement: Notes With AI Tools
#### Test TC033 — Create a note, save it, and generate a summary
- **Test Code:** [TC033_Create_a_note_save_it_and_generate_a_summary.py](./testsprite_tests/TC033_Create_a_note_save_it_and_generate_a_summary.py)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/42e3c45e-dfdb-450a-81cc-93cee907abc1/7a1f4e70-8792-4551-b621-10cc7a3629cf
- **Status:** ✅ Passed
- **Analysis / Findings:** Notes can be created and saved; summarize action produces an AI-generated summary in the editor (mock accepted).

#### Test TC034 — Saved note persists after page reload
- **Test Code:** [TC034_Saved_note_persists_after_page_reload.py](./testsprite_tests/TC034_Saved_note_persists_after_page_reload.py)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/42e3c45e-dfdb-450a-81cc-93cee907abc1/565c5d0e-9738-40df-8306-6a83eb541f2b
- **Status:** ✅ Passed
- **Analysis / Findings:** Notes saved to localStorage persist after a full page reload.

#### Test TC035 — Extract Tasks from a selected note adds tasks to the task list
- **Test Code:** [TC035_Extract_Tasks_from_a_selected_note_adds_tasks_to_the_task_list.py](./testsprite_tests/TC035_Extract_Tasks_from_a_selected_note_adds_tasks_to_the_task_list.py)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/42e3c45e-dfdb-450a-81cc-93cee907abc1/83e21113-ac3d-4b5b-85e0-e490f21e4dcd
- **Status:** ✅ Passed
- **Analysis / Findings:** Extract Tasks creates one or more new tasks from AI output and persists them to the task list.

#### Test TC038 — Saving an empty note is blocked with validation and does not add a note
- **Test Code:** [TC038_Saving_an_empty_note_is_blocked_with_validation_and_does_not_add_a_note.py](./testsprite_tests/TC038_Saving_an_empty_note_is_blocked_with_validation_and_does_not_add_a_note.py)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/42e3c45e-dfdb-450a-81cc-93cee907abc1/8825298c-7aa1-43b3-a840-c15b9a0cb5de
- **Status:** ✅ Passed
- **Analysis / Findings:** Saving with empty title+content is rejected and does not persist a blank note.

#### Test TC036 — Extracted tasks persist after reload
- **Test Code:** [TC036_Extracted_tasks_persist_after_reload.py](./testsprite_tests/TC036_Extracted_tasks_persist_after_reload.py)
- **Status:** ✅ Passed
- **Analysis / Findings:** Tasks created from notes survive a full page reload.

#### Test TC037 — Summarize on an empty note shows a user-facing validation error
- **Test Code:** [TC037_Summarize_on_an_empty_note_shows_a_user_facing_validation_error.py](./testsprite_tests/TC037_Summarize_on_an_empty_note_shows_a_user_facing_validation_error.py)
- **Status:** ✅ Passed
- **Analysis / Findings:** Summarize is blocked on empty content with a visible validation message.

#### Test TC039 — Selecting a note changes the visible note content in the editor/viewer
- **Test Code:** [TC039_Selecting_a_note_changes_the_visible_note_content_in_the_editorviewer.py](./testsprite_tests/TC039_Selecting_a_note_changes_the_visible_note_content_in_the_editorviewer.py)
- **Status:** ✅ Passed
- **Analysis / Findings:** Switching note selection updates the editor content (auto-save on switch enabled).

## 3️⃣ Coverage & Matching Metrics
- **Executed / Planned:** 39 / 39 (100.00%)
- **Pass Rate (executed):** 35 / 39 (89.74%)

| Requirement        | Planned Tests | Executed Tests | ✅ Passed | ❌ Failed |
|-------------------|--------------:|---------------:|---------:|---------:|
| Site Navigation   | 8             | 8              | 7        | 1        |
| Local Profile Login | 2           | 2              | 2        | 0        |
| Task Management   | 7             | 7              | 6        | 1        |
| AI Commander (Chat/Analyze/Autoprioritize) | 8 | 8 | 8 | 0 |
| Focus Timer       | 7             | 7              | 5        | 2        |
| Notes With AI Tools | 7           | 7              | 7        | 0        |

## 4️⃣ Key Gaps / Risks
- **Test reliability issues:** TC011/TC029/TC030 failures are driven by broken generated scripts (missing steps + contradictory assertions) and should be fixed via the TestSprite dashboard.
- **Spec/test mismatch:** TC005 expects Compare/Pitch to route to `/404.html`, but other tests validate them as valid pages; confirm intended behavior and update/remove TC005 accordingly.
- **AI edge cases:** Demo exhaustion, long-response handling, and invalid-key UX beyond basic error visibility can be expanded with additional targeted tests.
