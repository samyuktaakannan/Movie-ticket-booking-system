<!DOCTYPE html>
<!-- saved from url=(0061)https://github.com/reyashv/python/blob/main/tkinterproject.py -->
<html lang="en" data-color-mode="auto" data-light-theme="dark_high_contrast" data-dark-theme="light_colorblind" data-a11y-animated-images="system" data-turbo-loaded=""><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><style type="text/css">.turbo-progress-bar {
  position: fixed;
  display: block;
  top: 0;
  left: 0;
  height: 3px;
  background: #0076ff;
  z-index: 2147483647;
  transition:
    width 300ms ease-out,
    opacity 150ms 150ms ease-in;
  transform: translate3d(0, 0, 0);
}
</style>
    
  
  
  
  
  
  

  <link crossorigin="anonymous" media="all" rel="stylesheet" href="./tinker_ui_files/dark_high_contrast-188ef1de59e6.css"><link crossorigin="anonymous" media="all" rel="stylesheet" href="./tinker_ui_files/light_colorblind-527658dec362.css"><link data-color-theme="light" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light-719f1193e0c0.css"><link data-color-theme="dark" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark-0c343b529849.css"><link data-color-theme="dark_dimmed" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_dimmed-f22da508b62a.css"><link data-color-theme="dark_colorblind" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_colorblind-bc6bf4eea850.css"><link data-color-theme="light_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_high_contrast-c7a7fe0cd8ec.css"><link data-color-theme="light_tritanopia" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_tritanopia-6aa855bdae0f.css"><link data-color-theme="dark_tritanopia" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_tritanopia-6aa5e25aacc0.css">
  
  
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="./tinker_ui_files/primer-1677771a5a91.css">
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="./tinker_ui_files/global-351bab218fd9.css">
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="./tinker_ui_files/github-b27b810a3ca1.css">
  <link crossorigin="anonymous" media="all" rel="stylesheet" href="./tinker_ui_files/code-e60976b70279.css">

    


  <script crossorigin="anonymous" defer="defer" type="application/javascript" src="./tinker_ui_files/wp-runtime-0da5b24f4839.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./tinker_ui_files/vendors-node_modules_stacktrace-parser_dist_stack-trace-parser_esm_js-node_modules_github_bro-327bbf-fe611eb551b1.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./tinker_ui_files/ui_packages_soft-nav_soft-nav_ts-5b9c83d9bb14.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./tinker_ui_files/environment-60e751a864f8.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./tinker_ui_files/vendors-node_modules_github_selector-observer_dist_index_esm_js-2646a2c533e3.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./tinker_ui_files/vendors-node_modules_delegated-events_dist_index_js-node_modules_github_details-dialog-elemen-63debe-c04540d458d4.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./tinker_ui_files/vendors-node_modules_fzy_js_index_js-node_modules_github_markdown-toolbar-element_dist_index_js-e3de700a4c9d.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./tinker_ui_files/vendors-node_modules_github_auto-complete-element_dist_index_js-node_modules_github_catalyst_-6afc16-e779583c369f.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./tinker_ui_files/vendors-node_modules_github_relative-time-element_dist_index_js-52e1ce026ad1.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./tinker_ui_files/vendors-node_modules_github_file-attachment-element_dist_index_js-node_modules_github_text-ex-3415a8-7ecc10fb88d0.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./tinker_ui_files/vendors-node_modules_github_filter-input-element_dist_index_js-node_modules_github_remote-inp-79182d-befd2b2f5880.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./tinker_ui_files/vendors-node_modules_primer_view-components_app_components_primer_primer_js-node_modules_gith-6a1af4-feae509e11df.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./tinker_ui_files/github-elements-3cbd209f9bb3.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./tinker_ui_files/element-registry-d46d179ca77b.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./tinker_ui_files/vendors-node_modules_lit-html_lit-html_js-9d9fe1859ce5.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./tinker_ui_files/vendors-node_modules_manuelpuyol_turbo_dist_turbo_es2017-esm_js-4140d67f0cc2.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./tinker_ui_files/vendors-node_modules_github_mini-throttle_dist_index_js-node_modules_github_alive-client_dist-bf5aa2-424aa982deef.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./tinker_ui_files/vendors-node_modules_primer_behaviors_dist_esm_dimensions_js-node_modules_github_hotkey_dist_-9fc4f4-d434ddaf3207.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./tinker_ui_files/vendors-node_modules_color-convert_index_js-35b3ae68c408.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./tinker_ui_files/vendors-node_modules_github_remote-form_dist_index_js-node_modules_github_session-resume_dist-def857-2a32d97c93c5.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./tinker_ui_files/vendors-node_modules_github_paste-markdown_dist_index_esm_js-node_modules_github_quote-select-15ddcc-1512e06cfee0.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./tinker_ui_files/app_assets_modules_github_updatable-content_ts-430cacb5f7df.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./tinker_ui_files/app_assets_modules_github_behaviors_keyboard-shortcuts-helper_ts-app_assets_modules_github_be-b45fbf-966a43464127.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./tinker_ui_files/app_assets_modules_github_behaviors_task-list_ts-app_assets_modules_github_onfocus_ts-app_ass-dbc08c-845eee16e504.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./tinker_ui_files/app_assets_modules_github_behaviors_commenting_edit_ts-app_assets_modules_github_behaviors_ht-83c235-30c68bad2844.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./tinker_ui_files/behaviors-e85b42569bb2.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./tinker_ui_files/vendors-node_modules_delegated-events_dist_index_js-node_modules_github_catalyst_lib_index_js-06ff531-32d7d1e94817.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./tinker_ui_files/notifications-global-f5b58d24780b.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./tinker_ui_files/vendors-node_modules_optimizely_optimizely-sdk_dist_optimizely_browser_es_min_js-node_modules-3f2a9e-65eee21d1482.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./tinker_ui_files/optimizely-c8dd6a30245b.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./tinker_ui_files/vendors-node_modules_morphdom_dist_morphdom-esm_js-node_modules_github_template-parts_lib_index_js-58417dae193c.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./tinker_ui_files/vendors-node_modules_virtualized-list_es_index_js-node_modules_github_memoize_dist_esm_index_js-8496b7c4b809.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./tinker_ui_files/vendors-node_modules_github_remote-form_dist_index_js-node_modules_delegated-events_dist_inde-70450e-0370b887db62.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./tinker_ui_files/app_assets_modules_github_ref-selector_ts-7bdefeb88a1a.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./tinker_ui_files/codespaces-efac46c48fd5.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./tinker_ui_files/vendors-node_modules_github_filter-input-element_dist_index_js-node_modules_github_mini-throt-a33094-b03defd3289b.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./tinker_ui_files/vendors-node_modules_github_file-attachment-element_dist_index_js-node_modules_github_mini-th-85225b-af76b7097f8e.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./tinker_ui_files/repositories-1c8f58375b8b.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./tinker_ui_files/topic-suggestions-4acfbd6733d5.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./tinker_ui_files/code-menu-98e16c621b6a.js.download"></script>
  

  



  

    

  


    


  
  

  

    
  
  
  
  



  

  




  

    

  

    
    
      
      
    
    
    
      
      
      
    
      
      


        


      
      <script type="application/json" id="memex_keyboard_shortcuts_preference">"all"</script>

        

    


  <meta http-equiv="x-pjax-version" content="214a2b4d179f657a21aa1172711d773d06ade827b2157b04e88d4363a810aae3" data-turbo-track="reload">
  <meta http-equiv="x-pjax-csp-version" content="1e256041dc1b2b6714ea3821038945ca21078ebf137ba7c8d20236f1fd712a83" data-turbo-track="reload">
  <meta http-equiv="x-pjax-css-version" content="6abb6f32a9ef0a98cf9fd2abe941e720d0446ceaaa0e32f41f6899aa3040c28d" data-turbo-track="reload">
  <meta http-equiv="x-pjax-js-version" content="d817f1bce3d8bca4cf85f29944be749e6ffd4a48d2620bd5474669474cf48153" data-turbo-track="reload">

  

    
  

  



    
  


  

  

  

  
  
  





  

  <script type="application/javascript" src="./tinker_ui_files/vendors-node_modules_github_clipboard-copy-element_dist_index_esm_js-node_modules_github_remo-8e6bec-232430bfe6da.js.download"></script><script type="application/javascript" src="./tinker_ui_files/vendors-node_modules_github_mini-throttle_dist_decorators_js-node_modules_scroll-anchoring_di-e71893-cc1b30c51a28.js.download"></script><script type="application/javascript" src="./tinker_ui_files/app_assets_modules_github_diffs_blob-lines_ts-app_assets_modules_github_diffs_linkable-line-n-f96c66-95d6b0f01b2e.js.download"></script><script type="application/javascript" src="./tinker_ui_files/diffs-93769778be61.js.download"></script><link rel="dns-prefetch" href="https://github.githubassets.com/"><link rel="dns-prefetch" href="https://avatars.githubusercontent.com/"><link rel="dns-prefetch" href="https://github-cloud.s3.amazonaws.com/"><link rel="dns-prefetch" href="https://user-images.githubusercontent.com/"><link rel="preconnect" href="https://github.githubassets.com/" crossorigin=""><link rel="preconnect" href="https://avatars.githubusercontent.com/"><meta name="optimizely-datafile" content="{&quot;groups&quot;: [], &quot;environmentKey&quot;: &quot;production&quot;, &quot;rollouts&quot;: [], &quot;typedAudiences&quot;: [], &quot;projectId&quot;: &quot;16737760170&quot;, &quot;variables&quot;: [], &quot;featureFlags&quot;: [], &quot;experiments&quot;: [], &quot;version&quot;: &quot;4&quot;, &quot;audiences&quot;: [{&quot;conditions&quot;: &quot;[\&quot;or\&quot;, {\&quot;match\&quot;: \&quot;exact\&quot;, \&quot;name\&quot;: \&quot;$opt_dummy_attribute\&quot;, \&quot;type\&quot;: \&quot;custom_attribute\&quot;, \&quot;value\&quot;: \&quot;$opt_dummy_value\&quot;}]&quot;, &quot;id&quot;: &quot;$opt_dummy_audience&quot;, &quot;name&quot;: &quot;Optimizely-Generated Audience for Backwards Compatibility&quot;}], &quot;anonymizeIP&quot;: true, &quot;sdkKey&quot;: &quot;WTc6awnGuYDdG98CYRban&quot;, &quot;attributes&quot;: [{&quot;id&quot;: &quot;16822470375&quot;, &quot;key&quot;: &quot;user_id&quot;}, {&quot;id&quot;: &quot;17143601254&quot;, &quot;key&quot;: &quot;spammy&quot;}, {&quot;id&quot;: &quot;18175660309&quot;, &quot;key&quot;: &quot;organization_plan&quot;}, {&quot;id&quot;: &quot;18813001570&quot;, &quot;key&quot;: &quot;is_logged_in&quot;}, {&quot;id&quot;: &quot;19073851829&quot;, &quot;key&quot;: &quot;geo&quot;}, {&quot;id&quot;: &quot;20175462351&quot;, &quot;key&quot;: &quot;requestedCurrency&quot;}, {&quot;id&quot;: &quot;20785470195&quot;, &quot;key&quot;: &quot;country_code&quot;}, {&quot;id&quot;: &quot;21656311196&quot;, &quot;key&quot;: &quot;opened_downgrade_dialog&quot;}], &quot;botFiltering&quot;: false, &quot;accountId&quot;: &quot;16737760170&quot;, &quot;events&quot;: [{&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;17911811441&quot;, &quot;key&quot;: &quot;hydro_click.dashboard.teacher_toolbox_cta&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18124116703&quot;, &quot;key&quot;: &quot;submit.organizations.complete_sign_up&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18145892387&quot;, &quot;key&quot;: &quot;no_metric.tracked_outside_of_optimizely&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18178755568&quot;, &quot;key&quot;: &quot;click.org_onboarding_checklist.add_repo&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18180553241&quot;, &quot;key&quot;: &quot;submit.repository_imports.create&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18186103728&quot;, &quot;key&quot;: &quot;click.help.learn_more_about_repository_creation&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18188530140&quot;, &quot;key&quot;: &quot;test_event&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18191963644&quot;, &quot;key&quot;: &quot;click.empty_org_repo_cta.transfer_repository&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18195612788&quot;, &quot;key&quot;: &quot;click.empty_org_repo_cta.import_repository&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18210945499&quot;, &quot;key&quot;: &quot;click.org_onboarding_checklist.invite_members&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18211063248&quot;, &quot;key&quot;: &quot;click.empty_org_repo_cta.create_repository&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18215721889&quot;, &quot;key&quot;: &quot;click.org_onboarding_checklist.update_profile&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18224360785&quot;, &quot;key&quot;: &quot;click.org_onboarding_checklist.dismiss&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18234832286&quot;, &quot;key&quot;: &quot;submit.organization_activation.complete&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18252392383&quot;, &quot;key&quot;: &quot;submit.org_repository.create&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18257551537&quot;, &quot;key&quot;: &quot;submit.org_member_invitation.create&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18259522260&quot;, &quot;key&quot;: &quot;submit.organization_profile.update&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18564603625&quot;, &quot;key&quot;: &quot;view.classroom_select_organization&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18568612016&quot;, &quot;key&quot;: &quot;click.classroom_sign_in_click&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18572592540&quot;, &quot;key&quot;: &quot;view.classroom_name&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18574203855&quot;, &quot;key&quot;: &quot;click.classroom_create_organization&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18582053415&quot;, &quot;key&quot;: &quot;click.classroom_select_organization&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18589463420&quot;, &quot;key&quot;: &quot;click.classroom_create_classroom&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18591323364&quot;, &quot;key&quot;: &quot;click.classroom_create_first_classroom&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18591652321&quot;, &quot;key&quot;: &quot;click.classroom_grant_access&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18607131425&quot;, &quot;key&quot;: &quot;view.classroom_creation&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18831680583&quot;, &quot;key&quot;: &quot;upgrade_account_plan&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;19064064515&quot;, &quot;key&quot;: &quot;click.signup&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;19075373687&quot;, &quot;key&quot;: &quot;click.view_account_billing_page&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;19077355841&quot;, &quot;key&quot;: &quot;click.dismiss_signup_prompt&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;19079713938&quot;, &quot;key&quot;: &quot;click.contact_sales&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;19120963070&quot;, &quot;key&quot;: &quot;click.compare_account_plans&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;19151690317&quot;, &quot;key&quot;: &quot;click.upgrade_account_cta&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;19424193129&quot;, &quot;key&quot;: &quot;click.open_account_switcher&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;19520330825&quot;, &quot;key&quot;: &quot;click.visit_account_profile&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;19540970635&quot;, &quot;key&quot;: &quot;click.switch_account_context&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;19730198868&quot;, &quot;key&quot;: &quot;submit.homepage_signup&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;19820830627&quot;, &quot;key&quot;: &quot;click.homepage_signup&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;19988571001&quot;, &quot;key&quot;: &quot;click.create_enterprise_trial&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20036538294&quot;, &quot;key&quot;: &quot;click.create_organization_team&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20040653299&quot;, &quot;key&quot;: &quot;click.input_enterprise_trial_form&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20062030003&quot;, &quot;key&quot;: &quot;click.continue_with_team&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20068947153&quot;, &quot;key&quot;: &quot;click.create_organization_free&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20086636658&quot;, &quot;key&quot;: &quot;click.signup_continue.username&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20091648988&quot;, &quot;key&quot;: &quot;click.signup_continue.create_account&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20103637615&quot;, &quot;key&quot;: &quot;click.signup_continue.email&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20111574253&quot;, &quot;key&quot;: &quot;click.signup_continue.password&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20120044111&quot;, &quot;key&quot;: &quot;view.pricing_page&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20152062109&quot;, &quot;key&quot;: &quot;submit.create_account&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20165800992&quot;, &quot;key&quot;: &quot;submit.upgrade_payment_form&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20171520319&quot;, &quot;key&quot;: &quot;submit.create_organization&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20222645674&quot;, &quot;key&quot;: &quot;click.recommended_plan_in_signup.discuss_your_needs&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20227443657&quot;, &quot;key&quot;: &quot;submit.verify_primary_user_email&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20234607160&quot;, &quot;key&quot;: &quot;click.recommended_plan_in_signup.try_enterprise&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20238175784&quot;, &quot;key&quot;: &quot;click.recommended_plan_in_signup.team&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20239847212&quot;, &quot;key&quot;: &quot;click.recommended_plan_in_signup.continue_free&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20251097193&quot;, &quot;key&quot;: &quot;recommended_plan&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20438619534&quot;, &quot;key&quot;: &quot;click.pricing_calculator.1_member&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20456699683&quot;, &quot;key&quot;: &quot;click.pricing_calculator.15_members&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20467868331&quot;, &quot;key&quot;: &quot;click.pricing_calculator.10_members&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20476267432&quot;, &quot;key&quot;: &quot;click.trial_days_remaining&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20476357660&quot;, &quot;key&quot;: &quot;click.discover_feature&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20479287901&quot;, &quot;key&quot;: &quot;click.pricing_calculator.custom_members&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20481107083&quot;, &quot;key&quot;: &quot;click.recommended_plan_in_signup.apply_teacher_benefits&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20483089392&quot;, &quot;key&quot;: &quot;click.pricing_calculator.5_members&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20484283944&quot;, &quot;key&quot;: &quot;click.onboarding_task&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20484996281&quot;, &quot;key&quot;: &quot;click.recommended_plan_in_signup.apply_student_benefits&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20486713726&quot;, &quot;key&quot;: &quot;click.onboarding_task_breadcrumb&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20490791319&quot;, &quot;key&quot;: &quot;click.upgrade_to_enterprise&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20491786766&quot;, &quot;key&quot;: &quot;click.talk_to_us&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20494144087&quot;, &quot;key&quot;: &quot;click.dismiss_enterprise_trial&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20499722759&quot;, &quot;key&quot;: &quot;completed_all_tasks&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20500710104&quot;, &quot;key&quot;: &quot;completed_onboarding_tasks&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20513160672&quot;, &quot;key&quot;: &quot;click.read_doc&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20516196762&quot;, &quot;key&quot;: &quot;actions_enabled&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20518980986&quot;, &quot;key&quot;: &quot;click.dismiss_trial_banner&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20535446721&quot;, &quot;key&quot;: &quot;click.issue_actions_prompt.dismiss_prompt&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20557002247&quot;, &quot;key&quot;: &quot;click.issue_actions_prompt.setup_workflow&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20595070227&quot;, &quot;key&quot;: &quot;click.pull_request_setup_workflow&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20626600314&quot;, &quot;key&quot;: &quot;click.seats_input&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20642310305&quot;, &quot;key&quot;: &quot;click.decrease_seats_number&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20662990045&quot;, &quot;key&quot;: &quot;click.increase_seats_number&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20679620969&quot;, &quot;key&quot;: &quot;click.public_product_roadmap&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20761240940&quot;, &quot;key&quot;: &quot;click.dismiss_survey_banner&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20767210721&quot;, &quot;key&quot;: &quot;click.take_survey&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20795281201&quot;, &quot;key&quot;: &quot;click.archive_list&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20966790249&quot;, &quot;key&quot;: &quot;contact_sales.submit&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20996500333&quot;, &quot;key&quot;: &quot;contact_sales.existing_customer&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20996890162&quot;, &quot;key&quot;: &quot;contact_sales.blank_message_field&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;21000470317&quot;, &quot;key&quot;: &quot;contact_sales.personal_email&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;21002790172&quot;, &quot;key&quot;: &quot;contact_sales.blank_phone_field&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;21354412592&quot;, &quot;key&quot;: &quot;click.dismiss_create_readme&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;21366102546&quot;, &quot;key&quot;: &quot;click.dismiss_zero_user_content&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;21370252505&quot;, &quot;key&quot;: &quot;account_did_downgrade&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;21370840408&quot;, &quot;key&quot;: &quot;click.cta_create_readme&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;21375451068&quot;, &quot;key&quot;: &quot;click.cta_create_new_repository&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;21385390948&quot;, &quot;key&quot;: &quot;click.zero_user_content&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;21467712175&quot;, &quot;key&quot;: &quot;click.downgrade_keep&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;21484112202&quot;, &quot;key&quot;: &quot;click.downgrade&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;21495292213&quot;, &quot;key&quot;: &quot;click.downgrade_survey_exit&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;21508241468&quot;, &quot;key&quot;: &quot;click.downgrade_survey_submit&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;21512030356&quot;, &quot;key&quot;: &quot;click.downgrade_support&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;21539090022&quot;, &quot;key&quot;: &quot;click.downgrade_exit&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;21543640644&quot;, &quot;key&quot;: &quot;click_fetch_upstream&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;21646510300&quot;, &quot;key&quot;: &quot;click.move_your_work&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;21656151116&quot;, &quot;key&quot;: &quot;click.add_branch_protection_rule&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;21663860599&quot;, &quot;key&quot;: &quot;click.downgrade_dialog_open&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;21687860483&quot;, &quot;key&quot;: &quot;click.learn_about_protected_branches&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;21689050333&quot;, &quot;key&quot;: &quot;click.dismiss_protect_this_branch&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;21864370109&quot;, &quot;key&quot;: &quot;click.sign_in&quot;}], &quot;revision&quot;: &quot;1372&quot;}"><title>python/tkinterproject.py at main · reyashv/python</title><meta name="route-pattern" content="/:user_id/:repository"><meta name="google-site-verification" content="c1kuD-K2HIVF635lypcsWPoD4kilo5-jA_wBFyT4uMY"><meta name="google-site-verification" content="KT5gs8h0wvaagLKAVWq8bbeNwnZZK1r1XQysX3xurLU"><meta name="google-site-verification" content="ZzhVyEFwb7w3e0-uOTltm8Jsck2F5StVihD0exw2fsA"><meta name="google-site-verification" content="GXs5KoUUkNCoaAZn7wPN-t01Pywp9M3sEjnt_3_ZWPc"><meta name="google-site-verification" content="Apib7-x98H0j5cPqHWwSMm6dNU4GmODRoqxLiDzdx9I"><meta name="octolytics-url" content="https://collector.github.com/github/collect"><meta name="octolytics-actor-id" content="124596951"><meta name="octolytics-actor-login" content="samyuktaakannan"><meta name="octolytics-actor-hash" content="d22996025fa85a82ec7f569adf319b6fb088845a1ff3b208901cd8bc01d768c5"><meta name="user-login" content="samyuktaakannan"><link rel="sudo-modal" href="https://github.com/sessions/sudo_modal"><meta name="viewport" content="width=device-width"><meta name="description" content="Contribute to reyashv/python development by creating an account on GitHub."><link rel="search" type="application/opensearchdescription+xml" href="https://github.com/opensearch.xml" title="GitHub"><link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub"><meta property="fb:app_id" content="1401488693436528"><meta name="apple-itunes-app" content="app-id=1477376905"><meta name="twitter:image:src" content="https://avatars.githubusercontent.com/u/97713189?s=400&amp;v=4"><meta name="twitter:site" content="@github"><meta name="twitter:card" content="summary"><meta name="twitter:title" content="reyashv/python"><meta name="twitter:description" content="Contribute to reyashv/python development by creating an account on GitHub."><meta property="og:image" content="https://avatars.githubusercontent.com/u/97713189?s=400&amp;v=4"><meta property="og:image:alt" content="Contribute to reyashv/python development by creating an account on GitHub."><meta property="og:site_name" content="GitHub"><meta property="og:type" content="object"><meta property="og:title" content="reyashv/python"><meta property="og:url" content="https://github.com/reyashv/python"><meta property="og:description" content="Contribute to reyashv/python development by creating an account on GitHub."><link rel="assets" href="https://github.githubassets.com/"><link rel="shared-web-socket" href="wss://alive.github.com/_sockets/u/124596951/ws?session=eyJ2IjoiVjMiLCJ1IjoxMjQ1OTY5NTEsInMiOjEwNTkwMTMwOTcsImMiOjE1NTc4Mzc3OTMsInQiOjE2Nzc2OTQ1ODR9--3062b444eb799c70cff7d7ae88db1b3b951779ff23663ff6cdde4808eace5797" data-refresh-url="/_alive" data-session-id="5ca9fb2b9003cb26e329832ffb57f6497decbdcb34753d0f08ba1ea0a24b882d"><link rel="shared-web-socket-src" href="https://github.com/assets-cdn/worker/socket-worker-d7c2fe14563a.js"><meta name="hostname" content="github.com"><meta name="keyboard-shortcuts-preference" content="all"><meta name="expected-hostname" content="github.com"><meta name="enabled-features" content="TURBO_EXPERIMENT_RISKY,IMAGE_METRIC_TRACKING,GEOJSON_AZURE_MAPS"><meta name="go-import" content="github.com/reyashv/python git https://github.com/reyashv/python.git"><meta name="octolytics-dimension-user_id" content="97713189"><meta name="octolytics-dimension-user_login" content="reyashv"><meta name="octolytics-dimension-repository_id" content="572068788"><meta name="octolytics-dimension-repository_nwo" content="reyashv/python"><meta name="octolytics-dimension-repository_public" content="false"><meta name="octolytics-dimension-repository_is_fork" content="false"><meta name="octolytics-dimension-repository_network_root_id" content="572068788"><meta name="octolytics-dimension-repository_network_root_nwo" content="reyashv/python"><meta name="turbo-body-classes" content="logged-in env-production page-responsive"><meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats"><meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors"><meta name="browser-optimizely-client-errors-url" content="https://api.github.com/_private/browser/optimizely_client/errors"><link rel="mask-icon" href="https://github.githubassets.com/pinned-octocat.svg" color="#000000"><link rel="alternate icon" class="js-site-favicon" type="image/png" href="https://github.githubassets.com/favicons/favicon.png"><link rel="icon" class="js-site-favicon" type="image/svg+xml" href="https://github.githubassets.com/favicons/favicon.svg"><meta name="theme-color" content="#1e2327"><meta name="color-scheme" content="light dark"><link rel="manifest" href="https://github.com/manifest.json" crossorigin="use-credentials"><meta name="selected-link" value="repo_source" data-turbo-transient=""><meta name="analytics-location" content="/&lt;user-name&gt;/&lt;repo-name&gt;/blob/show" data-turbo-transient=""><meta name="request-id" content="EFB6:171D:FA04:1FB386:63FF9679" data-turbo-transient=""><meta name="html-safe-nonce" content="2aad85880bcb91e2a4c362d6dfb557b4c11ce1932d1f7ba5859b6d1fc2dc9f6e" data-turbo-transient=""><meta name="visitor-payload" content="eyJyZWZlcnJlciI6Imh0dHBzOi8vZ2l0aHViLmNvbS9yZXlhc2h2L3B5dGhvbiIsInJlcXVlc3RfaWQiOiJFRkI2OjE3MUQ6RkEwNDoxRkIzODY6NjNGRjk2NzkiLCJ2aXNpdG9yX2lkIjoiODMxMTMzNDMyODc3MTg1MjIzMCIsInJlZ2lvbl9lZGdlIjoiY2VudHJhbGluZGlhIiwicmVnaW9uX3JlbmRlciI6ImlhZCJ9" data-turbo-transient=""><meta name="visitor-hmac" content="3427a76076fff262daf42db4763f305935ad2ef3e8a38160b847f7e34adaad4e" data-turbo-transient=""><meta name="github-keyboard-shortcuts" content="repository,source-code,file-tree" data-turbo-transient=""><meta name="hovercard-subject-tag" content="repository:572068788" data-turbo-transient=""><meta name="turbo-cache-control" content="no-preview" data-turbo-transient=""><link rel="canonical" href="https://github.com/reyashv/python/blob/main/tkinterproject.py" data-turbo-transient=""></head>

  <body class="logged-in env-production page-responsive page-blob" style="word-wrap: break-word;">
    <div data-turbo-body="" class="logged-in env-production page-responsive page-blob" style="word-wrap: break-word;">
      


    <div class="position-relative js-header-wrapper ">
      <a href="https://github.com/reyashv/python/blob/main/tkinterproject.py#start-of-content" class="p-3 color-bg-accent-emphasis color-fg-on-emphasis show-on-focus js-skip-to-content">Skip to content</a>
      <span data-view-component="true" class="progress-pjax-loader Progress position-fixed width-full">
    <span style="width: 0%;" data-view-component="true" class="Progress-item progress-pjax-loader-bar left-0 top-0 color-bg-accent-emphasis"></span>
</span>      
      


        <script crossorigin="anonymous" defer="defer" type="application/javascript" src="./tinker_ui_files/vendors-node_modules_github_mini-throttle_dist_decorators_js-node_modules_github_command-pale-4090c9-7e4f6807221c.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./tinker_ui_files/vendors-node_modules_github_clipboard-copy-element_dist_index_esm_js-node_modules_delegated-e-b37f7d-dc7d4f29933c.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./tinker_ui_files/app_assets_modules_github_command-palette_items_help-item_ts-app_assets_modules_github_comman-48ad9d-3915025753ca.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./tinker_ui_files/command-palette-07aa94f1c0d8.js.download"></script>

            <header class="Header js-details-container Details px-3 px-md-4 px-lg-5 flex-wrap flex-md-nowrap" role="banner">

    <div class="Header-item mt-n1 mb-n1  d-none d-md-flex">
      <a class="Header-link" href="https://github.com/" data-hotkey="g d" aria-label="Homepage " data-turbo="false" data-analytics-event="{&quot;category&quot;:&quot;Header&quot;,&quot;action&quot;:&quot;go to dashboard&quot;,&quot;label&quot;:&quot;icon:logo&quot;}">
  <svg height="32" aria-hidden="true" viewBox="0 0 16 16" version="1.1" width="32" data-view-component="true" class="octicon octicon-mark-github v-align-middle">
    <path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"></path>
</svg>
</a>

    </div>

    <div class="Header-item d-md-none">
        <button aria-label="Toggle navigation" aria-expanded="false" type="button" data-view-component="true" class="Header-link js-details-target btn-link">    <svg aria-hidden="true" height="24" viewBox="0 0 16 16" version="1.1" width="24" data-view-component="true" class="octicon octicon-three-bars">
    <path fill-rule="evenodd" d="M1 2.75A.75.75 0 011.75 2h12.5a.75.75 0 110 1.5H1.75A.75.75 0 011 2.75zm0 5A.75.75 0 011.75 7h12.5a.75.75 0 110 1.5H1.75A.75.75 0 011 7.75zM1.75 12a.75.75 0 100 1.5h12.5a.75.75 0 100-1.5H1.75z"></path>
</svg>
</button>    </div>

    <div class="Header-item Header-item--full flex-column flex-md-row width-full flex-order-2 flex-md-order-none mr-0 mt-3 mt-md-0 Details-content--hidden-not-important d-md-flex">
              



<div class="header-search flex-auto position-relative js-site-search flex-self-stretch flex-md-self-auto mb-3 mb-md-0 mr-0 mr-md-3 scoped-search site-scoped-search js-jump-to">
  <div class="position-relative">
    <!-- '"` --><!-- </textarea></xmp> --><form class="js-site-search-form" role="search" aria-label="Site" data-scope-type="Repository" data-scope-id="572068788" data-scoped-search-url="/reyashv/python/search" data-owner-scoped-search-url="/users/reyashv/search" data-unscoped-search-url="/search" data-turbo="false" action="https://github.com/reyashv/python/search" accept-charset="UTF-8" method="get">
      <label class="form-control header-search-wrapper input-sm p-0 js-chromeless-input-container header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center">
        <input type="text" class="form-control js-site-search-focus header-search-input jump-to-field js-jump-to-field js-site-search-field is-clearable" data-hotkey="s,/" name="q" placeholder="Search or jump to…" data-unscoped-placeholder="Search or jump to…" data-scoped-placeholder="Search or jump to…" autocapitalize="off" role="combobox" aria-haspopup="listbox" aria-expanded="false" aria-autocomplete="list" aria-controls="jump-to-results" aria-label="Search or jump to…" data-jump-to-suggestions-path="/_graphql/GetSuggestedNavigationDestinations" spellcheck="false" autocomplete="off">
        <input type="hidden" value="1D-AKtmRcdUzjkB_xv2MzqOt5nd2TrXb8S5zsrwEgl407v6PXg7LWW11xXHEpd79UeJi9Zpzh251swx13DmUrA" data-csrf="true" class="js-data-jump-to-suggestions-path-csrf">
        <input type="hidden" class="js-site-search-type-field" name="type">
            <svg xmlns="http://www.w3.org/2000/svg" width="22" height="20" aria-hidden="true" class="mr-1 header-search-key-slash"><path fill="none" stroke="#979A9C" opacity=".4" d="M3.5.5h12c1.7 0 3 1.3 3 3v13c0 1.7-1.3 3-3 3h-12c-1.7 0-3-1.3-3-3v-13c0-1.7 1.3-3 3-3z"></path><path fill="#979A9C" d="M11.8 6L8 15.1h-.9L10.8 6h1z"></path></svg>


          <div class="Box position-absolute overflow-hidden d-none jump-to-suggestions js-jump-to-suggestions-container">
            
<ul class="d-none js-jump-to-suggestions-template-container">
  

<li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-suggestion" role="option">
  <a tabindex="-1" class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="https://github.com/reyashv/python/blob/main/tkinterproject.py" data-item-type="suggestion">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
      <svg title="Repository" aria-label="Repository" role="img" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo js-jump-to-octicon-repo d-none flex-shrink-0">
    <path fill-rule="evenodd" d="M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 110-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8zM5 12.25v3.25a.25.25 0 00.4.2l1.45-1.087a.25.25 0 01.3 0L8.6 15.7a.25.25 0 00.4-.2v-3.25a.25.25 0 00-.25-.25h-3.5a.25.25 0 00-.25.25z"></path>
</svg>
      <svg title="Project" aria-label="Project" role="img" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-project js-jump-to-octicon-project d-none flex-shrink-0">
    <path fill-rule="evenodd" d="M1.75 0A1.75 1.75 0 000 1.75v12.5C0 15.216.784 16 1.75 16h12.5A1.75 1.75 0 0016 14.25V1.75A1.75 1.75 0 0014.25 0H1.75zM1.5 1.75a.25.25 0 01.25-.25h12.5a.25.25 0 01.25.25v12.5a.25.25 0 01-.25.25H1.75a.25.25 0 01-.25-.25V1.75zM11.75 3a.75.75 0 00-.75.75v7.5a.75.75 0 001.5 0v-7.5a.75.75 0 00-.75-.75zm-8.25.75a.75.75 0 011.5 0v5.5a.75.75 0 01-1.5 0v-5.5zM8 3a.75.75 0 00-.75.75v3.5a.75.75 0 001.5 0v-3.5A.75.75 0 008 3z"></path>
</svg>
      <svg title="Search" aria-label="Search" role="img" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search js-jump-to-octicon-search d-none flex-shrink-0">
    <path fill-rule="evenodd" d="M11.5 7a4.499 4.499 0 11-8.998 0A4.499 4.499 0 0111.5 7zm-.82 4.74a6 6 0 111.06-1.06l3.04 3.04a.75.75 0 11-1.06 1.06l-3.04-3.04z"></path>
</svg>
    </div>

    <img class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" alt="" aria-label="Team" src="https://github.com/reyashv/python/blob/main/tkinterproject.py" width="28" height="28">

    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>

    <div class="border rounded-2 flex-shrink-0 color-bg-subtle px-1 color-fg-muted ml-1 f6 d-none js-jump-to-badge-search">
      <span class="js-jump-to-badge-search-text-default d-none" aria-label="in this repository">
        In this repository
      </span>
      <span class="js-jump-to-badge-search-text-global d-none" aria-label="in all of GitHub">
        All GitHub
      </span>
      <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>

    <div aria-hidden="true" class="border rounded-2 flex-shrink-0 color-bg-subtle px-1 color-fg-muted ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
      Jump to
      <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
  </a>
</li>

</ul>

<ul class="d-none js-jump-to-no-results-template-container">
  <li class="d-flex flex-justify-center flex-items-center f5 d-none js-jump-to-suggestion p-2">
    <span class="color-fg-muted">No suggested jump to results</span>
  </li>
</ul>

<ul id="jump-to-results" role="listbox" class="p-0 m-0 js-navigation-container jump-to-suggestions-results-container js-jump-to-suggestions-results-container">
  

<li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-scoped-search d-none" role="option">
  <a tabindex="-1" class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="https://github.com/reyashv/python/blob/main/tkinterproject.py" data-item-type="scoped_search">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
      <svg title="Repository" aria-label="Repository" role="img" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo js-jump-to-octicon-repo d-none flex-shrink-0">
    <path fill-rule="evenodd" d="M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 110-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8zM5 12.25v3.25a.25.25 0 00.4.2l1.45-1.087a.25.25 0 01.3 0L8.6 15.7a.25.25 0 00.4-.2v-3.25a.25.25 0 00-.25-.25h-3.5a.25.25 0 00-.25.25z"></path>
</svg>
      <svg title="Project" aria-label="Project" role="img" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-project js-jump-to-octicon-project d-none flex-shrink-0">
    <path fill-rule="evenodd" d="M1.75 0A1.75 1.75 0 000 1.75v12.5C0 15.216.784 16 1.75 16h12.5A1.75 1.75 0 0016 14.25V1.75A1.75 1.75 0 0014.25 0H1.75zM1.5 1.75a.25.25 0 01.25-.25h12.5a.25.25 0 01.25.25v12.5a.25.25 0 01-.25.25H1.75a.25.25 0 01-.25-.25V1.75zM11.75 3a.75.75 0 00-.75.75v7.5a.75.75 0 001.5 0v-7.5a.75.75 0 00-.75-.75zm-8.25.75a.75.75 0 011.5 0v5.5a.75.75 0 01-1.5 0v-5.5zM8 3a.75.75 0 00-.75.75v3.5a.75.75 0 001.5 0v-3.5A.75.75 0 008 3z"></path>
</svg>
      <svg title="Search" aria-label="Search" role="img" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search js-jump-to-octicon-search d-none flex-shrink-0">
    <path fill-rule="evenodd" d="M11.5 7a4.499 4.499 0 11-8.998 0A4.499 4.499 0 0111.5 7zm-.82 4.74a6 6 0 111.06-1.06l3.04 3.04a.75.75 0 11-1.06 1.06l-3.04-3.04z"></path>
</svg>
    </div>

    <img class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" alt="" aria-label="Team" src="https://github.com/reyashv/python/blob/main/tkinterproject.py" width="28" height="28">

    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>

    <div class="border rounded-2 flex-shrink-0 color-bg-subtle px-1 color-fg-muted ml-1 f6 d-none js-jump-to-badge-search">
      <span class="js-jump-to-badge-search-text-default d-none" aria-label="in this repository">
        In this repository
      </span>
      <span class="js-jump-to-badge-search-text-global d-none" aria-label="in all of GitHub">
        All GitHub
      </span>
      <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>

    <div aria-hidden="true" class="border rounded-2 flex-shrink-0 color-bg-subtle px-1 color-fg-muted ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
      Jump to
      <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
  </a>
</li>

  

<li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-owner-scoped-search d-none" role="option">
  <a tabindex="-1" class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="https://github.com/reyashv/python/blob/main/tkinterproject.py" data-item-type="owner_scoped_search">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
      <svg title="Repository" aria-label="Repository" role="img" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo js-jump-to-octicon-repo d-none flex-shrink-0">
    <path fill-rule="evenodd" d="M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 110-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8zM5 12.25v3.25a.25.25 0 00.4.2l1.45-1.087a.25.25 0 01.3 0L8.6 15.7a.25.25 0 00.4-.2v-3.25a.25.25 0 00-.25-.25h-3.5a.25.25 0 00-.25.25z"></path>
</svg>
      <svg title="Project" aria-label="Project" role="img" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-project js-jump-to-octicon-project d-none flex-shrink-0">
    <path fill-rule="evenodd" d="M1.75 0A1.75 1.75 0 000 1.75v12.5C0 15.216.784 16 1.75 16h12.5A1.75 1.75 0 0016 14.25V1.75A1.75 1.75 0 0014.25 0H1.75zM1.5 1.75a.25.25 0 01.25-.25h12.5a.25.25 0 01.25.25v12.5a.25.25 0 01-.25.25H1.75a.25.25 0 01-.25-.25V1.75zM11.75 3a.75.75 0 00-.75.75v7.5a.75.75 0 001.5 0v-7.5a.75.75 0 00-.75-.75zm-8.25.75a.75.75 0 011.5 0v5.5a.75.75 0 01-1.5 0v-5.5zM8 3a.75.75 0 00-.75.75v3.5a.75.75 0 001.5 0v-3.5A.75.75 0 008 3z"></path>
</svg>
      <svg title="Search" aria-label="Search" role="img" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search js-jump-to-octicon-search d-none flex-shrink-0">
    <path fill-rule="evenodd" d="M11.5 7a4.499 4.499 0 11-8.998 0A4.499 4.499 0 0111.5 7zm-.82 4.74a6 6 0 111.06-1.06l3.04 3.04a.75.75 0 11-1.06 1.06l-3.04-3.04z"></path>
</svg>
    </div>

    <img class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" alt="" aria-label="Team" src="https://github.com/reyashv/python/blob/main/tkinterproject.py" width="28" height="28">

    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>

    <div class="border rounded-2 flex-shrink-0 color-bg-subtle px-1 color-fg-muted ml-1 f6 d-none js-jump-to-badge-search">
      <span class="js-jump-to-badge-search-text-default d-none" aria-label="in this user">
        In this user
      </span>
      <span class="js-jump-to-badge-search-text-global d-none" aria-label="in all of GitHub">
        All GitHub
      </span>
      <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>

    <div aria-hidden="true" class="border rounded-2 flex-shrink-0 color-bg-subtle px-1 color-fg-muted ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
      Jump to
      <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
  </a>
</li>

  

<li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-global-search d-none" role="option">
  <a tabindex="-1" class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="https://github.com/reyashv/python/blob/main/tkinterproject.py" data-item-type="global_search">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
      <svg title="Repository" aria-label="Repository" role="img" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo js-jump-to-octicon-repo d-none flex-shrink-0">
    <path fill-rule="evenodd" d="M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 110-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8zM5 12.25v3.25a.25.25 0 00.4.2l1.45-1.087a.25.25 0 01.3 0L8.6 15.7a.25.25 0 00.4-.2v-3.25a.25.25 0 00-.25-.25h-3.5a.25.25 0 00-.25.25z"></path>
</svg>
      <svg title="Project" aria-label="Project" role="img" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-project js-jump-to-octicon-project d-none flex-shrink-0">
    <path fill-rule="evenodd" d="M1.75 0A1.75 1.75 0 000 1.75v12.5C0 15.216.784 16 1.75 16h12.5A1.75 1.75 0 0016 14.25V1.75A1.75 1.75 0 0014.25 0H1.75zM1.5 1.75a.25.25 0 01.25-.25h12.5a.25.25 0 01.25.25v12.5a.25.25 0 01-.25.25H1.75a.25.25 0 01-.25-.25V1.75zM11.75 3a.75.75 0 00-.75.75v7.5a.75.75 0 001.5 0v-7.5a.75.75 0 00-.75-.75zm-8.25.75a.75.75 0 011.5 0v5.5a.75.75 0 01-1.5 0v-5.5zM8 3a.75.75 0 00-.75.75v3.5a.75.75 0 001.5 0v-3.5A.75.75 0 008 3z"></path>
</svg>
      <svg title="Search" aria-label="Search" role="img" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search js-jump-to-octicon-search d-none flex-shrink-0">
    <path fill-rule="evenodd" d="M11.5 7a4.499 4.499 0 11-8.998 0A4.499 4.499 0 0111.5 7zm-.82 4.74a6 6 0 111.06-1.06l3.04 3.04a.75.75 0 11-1.06 1.06l-3.04-3.04z"></path>
</svg>
    </div>

    <img class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" alt="" aria-label="Team" src="https://github.com/reyashv/python/blob/main/tkinterproject.py" width="28" height="28">

    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>

    <div class="border rounded-2 flex-shrink-0 color-bg-subtle px-1 color-fg-muted ml-1 f6 d-none js-jump-to-badge-search">
      <span class="js-jump-to-badge-search-text-default d-none" aria-label="in this repository">
        In this repository
      </span>
      <span class="js-jump-to-badge-search-text-global d-none" aria-label="in all of GitHub">
        All GitHub
      </span>
      <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>

    <div aria-hidden="true" class="border rounded-2 flex-shrink-0 color-bg-subtle px-1 color-fg-muted ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
      Jump to
      <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
  </a>
</li>


    <li class="d-flex flex-justify-center flex-items-center p-0 f5 js-jump-to-suggestion">
      <svg style="box-sizing: content-box; color: var(--color-icon-primary);" width="32" height="32" viewBox="0 0 16 16" fill="none" data-view-component="true" class="m-3 anim-rotate">
  <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke"></circle>
  <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke"></path>
</svg>
    </li>
</ul>

          </div>
      </label>
</form>  </div>
</div>

        <nav id="global-nav" class="d-flex flex-column flex-md-row flex-self-stretch flex-md-self-auto" aria-label="Global">
    <a class="Header-link py-md-3 d-block d-md-none py-2 border-top border-md-top-0 border-white-fade" data-ga-click="Header, click, Nav menu - item:dashboard:user" aria-label="Dashboard" data-turbo="false" href="https://github.com/dashboard">Dashboard</a>

  <a class="js-selected-navigation-item Header-link mt-md-n3 mb-md-n3 py-2 py-md-3 mr-0 mr-md-3 border-top border-md-top-0 border-white-fade" data-hotkey="g p" data-ga-click="Header, click, Nav menu - item:pulls context:user" aria-label="Pull requests you created" data-turbo="false" data-selected-links="/pulls /pulls/assigned /pulls/mentioned /pulls" href="https://github.com/pulls">
      Pull<span class="d-inline d-md-none d-lg-inline"> request</span>s
</a>
  <a class="js-selected-navigation-item Header-link mt-md-n3 mb-md-n3 py-2 py-md-3 mr-0 mr-md-3 border-top border-md-top-0 border-white-fade" data-hotkey="g i" data-ga-click="Header, click, Nav menu - item:issues context:user" aria-label="Issues you created" data-turbo="false" data-selected-links="/issues /issues/assigned /issues/mentioned /issues" href="https://github.com/issues">Issues</a>

      <a class="js-selected-navigation-item Header-link mt-md-n3 mb-md-n3 py-2 py-md-3 mr-0 mr-md-3 border-top border-md-top-0 border-white-fade" data-ga-click="Header, click, Nav menu - item:workspaces context:user" data-turbo="false" data-selected-links="/codespaces /codespaces" href="https://github.com/codespaces">Codespaces</a>

    <div class="d-flex position-relative">
      <a class="js-selected-navigation-item Header-link flex-auto mt-md-n3 mb-md-n3 py-2 py-md-3 mr-0 mr-md-3 border-top border-md-top-0 border-white-fade" data-ga-click="Header, click, Nav menu - item:marketplace context:user" data-octo-click="marketplace_click" data-octo-dimensions="location:nav_bar" data-turbo="false" data-selected-links=" /marketplace" href="https://github.com/marketplace">Marketplace</a>
    </div>

  <a class="js-selected-navigation-item Header-link mt-md-n3 mb-md-n3 py-2 py-md-3 mr-0 mr-md-3 border-top border-md-top-0 border-white-fade" data-ga-click="Header, click, Nav menu - item:explore" data-turbo="false" data-selected-links="/explore /trending /trending/developers /integrations /integrations/feature/code /integrations/feature/collaborate /integrations/feature/ship showcases showcases_search showcases_landing /explore" href="https://github.com/explore">Explore</a>

      <a class="js-selected-navigation-item Header-link d-block d-md-none py-2 py-md-3 border-top border-md-top-0 border-white-fade" data-ga-click="Header, click, Nav menu - item:Sponsors" data-hydro-click="{&quot;event_type&quot;:&quot;sponsors.button_click&quot;,&quot;payload&quot;:{&quot;button&quot;:&quot;HEADER_SPONSORS_DASHBOARD&quot;,&quot;sponsorable_login&quot;:&quot;samyuktaakannan&quot;,&quot;originating_url&quot;:&quot;https://github.com/reyashv/python&quot;,&quot;user_id&quot;:124596951}}" data-hydro-click-hmac="65fa8495b8698d5890a2c99825dc79ca00fab640a12e660462ef1c4f82025982" data-turbo="false" data-selected-links=" /sponsors/accounts" href="https://github.com/sponsors/accounts">Sponsors</a>

    <a class="Header-link d-block d-md-none mr-0 mr-md-3 py-2 py-md-3 border-top border-md-top-0 border-white-fade" data-turbo="false" href="https://github.com/settings/profile">Settings</a>

    <a class="Header-link d-block d-md-none mr-0 mr-md-3 py-2 py-md-3 border-top border-md-top-0 border-white-fade" data-turbo="false" href="https://github.com/samyuktaakannan">
      <img class="avatar avatar-user" loading="lazy" decoding="async" src="./tinker_ui_files/124596951" width="20" height="20" alt="@samyuktaakannan">
      samyuktaakannan
</a>
    <!-- '"` --><!-- </textarea></xmp> --><form data-turbo="false" action="https://github.com/logout" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="_mf00Ixv9Iw-CyT-k81I1MzsjEY0Zh5vb5SLmGXssJIZzUdlb-dX_XBl6YvS73MAqW2bN8tgXkU5Q1xo8odASg">
      <button type="submit" class="Header-link mr-0 mr-md-3 py-2 py-md-3 border-top border-md-top-0 border-white-fade d-md-none btn-link d-block width-full text-left" style="padding-left: 2px;" data-analytics-event="{&quot;category&quot;:&quot;Header&quot;,&quot;action&quot;:&quot;sign out&quot;,&quot;label&quot;:&quot;icon:logout&quot;}">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-sign-out v-align-middle">
    <path fill-rule="evenodd" d="M2 2.75C2 1.784 2.784 1 3.75 1h2.5a.75.75 0 010 1.5h-2.5a.25.25 0 00-.25.25v10.5c0 .138.112.25.25.25h2.5a.75.75 0 010 1.5h-2.5A1.75 1.75 0 012 13.25V2.75zm10.44 4.5H6.75a.75.75 0 000 1.5h5.69l-1.97 1.97a.75.75 0 101.06 1.06l3.25-3.25a.75.75 0 000-1.06l-3.25-3.25a.75.75 0 10-1.06 1.06l1.97 1.97z"></path>
</svg>
        Sign out
      </button>
</form></nav>

    </div>

    <div class="Header-item Header-item--full flex-justify-center d-md-none position-relative">
        <a class="Header-link" href="https://github.com/" data-hotkey="g d" aria-label="Homepage " data-turbo="false" data-analytics-event="{&quot;category&quot;:&quot;Header&quot;,&quot;action&quot;:&quot;go to dashboard&quot;,&quot;label&quot;:&quot;icon:logo&quot;}">
  <svg height="32" aria-hidden="true" viewBox="0 0 16 16" version="1.1" width="32" data-view-component="true" class="octicon octicon-mark-github v-align-middle">
    <path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"></path>
</svg>
</a>

    </div>

    <div class="Header-item mr-0 mr-md-3 flex-order-1 flex-md-order-none">
        

<notification-indicator data-channel="eyJjIjoibm90aWZpY2F0aW9uLWNoYW5nZWQ6MTI0NTk2OTUxIiwidCI6MTY3NzY5NDU4NH0=--2d3e270a908bffecb9401bc40ee774fb0a02095b73b2061d04eb5d89874bd4eb" data-indicator-mode="none" data-tooltip-global="You have unread notifications" data-tooltip-unavailable="Notifications are unavailable at the moment." data-tooltip-none="You have no unread notifications" data-fetch-indicator-src="/notifications/indicator" data-fetch-indicator-enabled="true" data-view-component="true" class="js-socket-channel" data-fetch-retry-delay-time="500" data-catalyst="">
  <a id="AppHeader-notifications-button" href="https://github.com/notifications" class="Header-link notification-indicator position-relative tooltipped tooltipped-sw" data-hotkey="g n" data-target="notification-indicator.link" aria-label="You have no unread notifications" data-analytics-event="{&quot;category&quot;:&quot;Header&quot;,&quot;action&quot;:&quot;go to notifications&quot;,&quot;label&quot;:&quot;icon:read&quot;}">

    <span data-target="notification-indicator.badge" class="mail-status unread" hidden="">
    </span>

      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-bell">
    <path d="M8 16a2 2 0 001.985-1.75c.017-.137-.097-.25-.235-.25h-3.5c-.138 0-.252.113-.235.25A2 2 0 008 16z"></path><path fill-rule="evenodd" d="M8 1.5A3.5 3.5 0 004.5 5v2.947c0 .346-.102.683-.294.97l-1.703 2.556a.018.018 0 00-.003.01l.001.006c0 .002.002.004.004.006a.017.017 0 00.006.004l.007.001h10.964l.007-.001a.016.016 0 00.006-.004.016.016 0 00.004-.006l.001-.007a.017.017 0 00-.003-.01l-1.703-2.554a1.75 1.75 0 01-.294-.97V5A3.5 3.5 0 008 1.5zM3 5a5 5 0 0110 0v2.947c0 .05.015.098.042.139l1.703 2.555A1.518 1.518 0 0113.482 13H2.518a1.518 1.518 0 01-1.263-2.36l1.703-2.554A.25.25 0 003 7.947V5z"></path>
</svg>
  </a>

</notification-indicator>
    </div>


    <div class="Header-item position-relative d-none d-md-flex">
        <details class="details-overlay details-reset">
  <summary class="Header-link" aria-label="Create new…" data-analytics-event="{&quot;category&quot;:&quot;Header&quot;,&quot;action&quot;:&quot;create new&quot;,&quot;label&quot;:&quot;icon:add&quot;}" aria-haspopup="menu" role="button">
    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path fill-rule="evenodd" d="M7.75 2a.75.75 0 01.75.75V7h4.25a.75.75 0 110 1.5H8.5v4.25a.75.75 0 11-1.5 0V8.5H2.75a.75.75 0 010-1.5H7V2.75A.75.75 0 017.75 2z"></path>
</svg> <span class="dropdown-caret"></span>
  </summary>
  <details-menu class="dropdown-menu dropdown-menu-sw" role="menu" data-focus-trap="suspended"><span class="sentinel" tabindex="0" aria-hidden="true"></span>
    
<a role="menuitem" class="dropdown-item" href="https://github.com/new" data-ga-click="Header, create new repository">
  New repository
</a>

  <a role="menuitem" class="dropdown-item" href="https://github.com/new/import" data-ga-click="Header, import a repository">
    Import repository
  </a>

  <a role="menuitem" class="dropdown-item" href="https://github.com/codespaces/new">
    New codespace
  </a>

<a role="menuitem" class="dropdown-item" href="https://gist.github.com/" data-ga-click="Header, create new gist">
  New gist
</a>

  <a role="menuitem" class="dropdown-item" href="https://github.com/organizations/new" data-ga-click="Header, create new organization">
    New organization
  </a>



  <span class="sentinel" tabindex="0" aria-hidden="true"></span></details-menu>
</details>

    </div>

    <div class="Header-item position-relative mr-0 d-none d-md-flex">
        
  <details class="details-overlay details-reset js-feature-preview-indicator-container" data-feature-preview-indicator-src="/users/samyuktaakannan/feature_preview/indicator_check">

  <summary class="Header-link" aria-label="View profile and more" data-analytics-event="{&quot;category&quot;:&quot;Header&quot;,&quot;action&quot;:&quot;show menu&quot;,&quot;label&quot;:&quot;icon:avatar&quot;}" aria-haspopup="menu" role="button">
    <img src="./tinker_ui_files/124596951" alt="@samyuktaakannan" size="20" height="20" width="20" data-view-component="true" class="avatar avatar-small circle">
      <span class="unread-indicator js-feature-preview-indicator" style="top: 1px;"></span>
    <span class="dropdown-caret"></span>
  </summary>
  <details-menu class="dropdown-menu dropdown-menu-sw" style="width: 180px" preload="" role="menu" data-focus-trap="suspended"><span class="sentinel" tabindex="0" aria-hidden="true"></span>
      <include-fragment src="/users/124596951/menu" loading="lazy">
        <p class="text-center mt-3" data-hide-on-error="">
          <svg style="box-sizing: content-box; color: var(--color-icon-primary);" width="32" height="32" viewBox="0 0 16 16" fill="none" data-view-component="true" class="anim-rotate">
  <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke"></circle>
  <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke"></path>
</svg>
        </p>
        <p class="ml-1 mb-2 mt-2 color-fg-default" data-show-on-error="">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert">
    <path fill-rule="evenodd" d="M8.22 1.754a.25.25 0 00-.44 0L1.698 13.132a.25.25 0 00.22.368h12.164a.25.25 0 00.22-.368L8.22 1.754zm-1.763-.707c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0114.082 15H1.918a1.75 1.75 0 01-1.543-2.575L6.457 1.047zM9 11a1 1 0 11-2 0 1 1 0 012 0zm-.25-5.25a.75.75 0 00-1.5 0v2.5a.75.75 0 001.5 0v-2.5z"></path>
</svg>
          Sorry, something went wrong.
        </p>
      </include-fragment>
  <span class="sentinel" tabindex="0" aria-hidden="true"></span></details-menu>
</details>

    </div>
</header>

            
    </div>

  <div id="start-of-content" class="show-on-focus"></div>







    <div id="js-flash-container" data-turbo-replace="">





  <template class="js-flash-template"></template>
</div>


    
    <notification-shelf-watcher data-base-url="https://github.com/notifications/beta/shelf" data-channel="eyJjIjoibm90aWZpY2F0aW9uLWNoYW5nZWQ6MTI0NTk2OTUxIiwidCI6MTY3NzY5NDU4NH0=--2d3e270a908bffecb9401bc40ee774fb0a02095b73b2061d04eb5d89874bd4eb" data-view-component="true" class="js-socket-channel" data-refresh-delay="500" data-catalyst=""></notification-shelf-watcher>
  <div hidden="" data-initial="" data-target="notification-shelf-watcher.placeholder"></div>






      <details class="details-reset details-overlay details-overlay-dark js-command-palette-dialog" id="command-palette-pjax-container" data-turbo-replace="">
  <summary aria-label="command palette trigger" tabindex="-1" role="button"></summary>
  <details-dialog class="command-palette-details-dialog d-flex flex-column flex-justify-center height-fit" aria-label="command palette" role="dialog" aria-modal="true">
    <command-palette class="command-palette color-bg-default rounded-3 border color-shadow-small" return-to="/reyashv/python/blob/main/tkinterproject.py" user-id="124596951" activation-hotkey="Mod+k,Mod+Alt+k" command-mode-hotkey="Mod+Shift+k" data-action="
        command-palette-input-ready:command-palette#inputReady
        command-palette-page-stack-updated:command-palette#updateInputScope
        itemsUpdated:command-palette#itemsUpdated
        keydown:command-palette#onKeydown
        loadingStateChanged:command-palette#loadingStateChanged
        selectedItemChanged:command-palette#selectedItemChanged
        pageFetchError:command-palette#pageFetchError
      " data-catalyst="">

        <command-palette-mode data-char="#" data-scope-types="[&quot;&quot;]" data-placeholder="Search issues and pull requests" data-catalyst=""></command-palette-mode>
        <command-palette-mode data-char="#" data-scope-types="[&quot;owner&quot;,&quot;repository&quot;]" data-placeholder="Search issues, pull requests, discussions, and projects" data-catalyst=""></command-palette-mode>
        <command-palette-mode data-char="!" data-scope-types="[&quot;owner&quot;,&quot;repository&quot;]" data-placeholder="Search projects" data-catalyst=""></command-palette-mode>
        <command-palette-mode data-char="@" data-scope-types="[&quot;&quot;]" data-placeholder="Search or jump to a user, organization, or repository" data-catalyst=""></command-palette-mode>
        <command-palette-mode data-char="@" data-scope-types="[&quot;owner&quot;]" data-placeholder="Search or jump to a repository" data-catalyst=""></command-palette-mode>
        <command-palette-mode data-char="/" data-scope-types="[&quot;repository&quot;]" data-placeholder="Search files" data-catalyst=""></command-palette-mode>
        <command-palette-mode data-char="?" data-placeholder="" data-catalyst="" data-scope-types=""></command-palette-mode>
        <command-palette-mode data-char="&gt;" data-placeholder="Run a command" data-scope-types="" data-catalyst=""></command-palette-mode>
        <command-palette-mode data-char="" data-scope-types="[&quot;&quot;]" data-placeholder="Search or jump to..." data-catalyst=""></command-palette-mode>
        <command-palette-mode data-char="" data-scope-types="[&quot;owner&quot;]" data-placeholder="Search or jump to..." data-catalyst=""></command-palette-mode>
      <command-palette-mode class="js-command-palette-default-mode" data-char="" data-placeholder="Search or jump to..." data-scope-types="" data-catalyst=""></command-palette-mode>

      <command-palette-input placeholder="Search or jump to..." data-action="
          command-palette-input:command-palette#onInput
          command-palette-select:command-palette#onSelect
          command-palette-descope:command-palette#onDescope
          command-palette-cleared:command-palette#onInputClear
        " data-catalyst="" class="d-flex flex-items-center flex-nowrap py-1 pl-3 pr-2 border-bottom">
        <div class="js-search-icon d-flex flex-items-center mr-2" style="height: 26px">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search color-fg-muted">
    <path fill-rule="evenodd" d="M11.5 7a4.499 4.499 0 11-8.998 0A4.499 4.499 0 0111.5 7zm-.82 4.74a6 6 0 111.06-1.06l3.04 3.04a.75.75 0 11-1.06 1.06l-3.04-3.04z"></path>
</svg>
        </div>
        <div class="js-spinner d-flex flex-items-center mr-2 color-fg-muted" hidden="">
          <svg aria-label="Loading" class="anim-rotate" viewBox="0 0 16 16" fill="none" width="16" height="16">
            <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke"></circle>
            <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke"></path>
          </svg>
        </div>
        <command-palette-scope data-catalyst="" class="d-inline-flex">
          <div data-target="command-palette-scope.placeholder" hidden="" class="color-fg-subtle">/&nbsp;&nbsp;<span class="text-semibold color-fg-default">...</span>&nbsp;&nbsp;/&nbsp;&nbsp;</div>
              <command-palette-token data-text="reyashv" data-id="U_kgDOBdL8JQ" data-type="owner" data-value="reyashv" data-targets="command-palette-scope.tokens" class="color-fg-default text-semibold" style="white-space:nowrap;line-height:20px;" id="" data-catalyst="">reyashv<span class="color-fg-subtle text-normal">&nbsp;&nbsp;/&nbsp;&nbsp;</span></command-palette-token>
              <command-palette-token data-text="python" data-id="R_kgDOIhkTtA" data-type="repository" data-value="python" data-targets="command-palette-scope.tokens" class="color-fg-default text-semibold" style="white-space:nowrap;line-height:20px;" id="" data-catalyst="">python<span class="color-fg-subtle text-normal">&nbsp;&nbsp;/&nbsp;&nbsp;</span></command-palette-token>
        </command-palette-scope>
        <div class="command-palette-input-group flex-1 form-control border-0 box-shadow-none" style="z-index: 0">
          <div class="command-palette-typeahead position-absolute d-flex flex-items-center Truncate">
            <span class="typeahead-segment input-mirror" data-target="command-palette-input.mirror"></span>
            <span class="Truncate-text" data-target="command-palette-input.typeaheadText"></span>
            <span class="typeahead-segment" data-target="command-palette-input.typeaheadPlaceholder"></span>
          </div>
          <input class="js-overlay-input typeahead-input d-none" disabled="" tabindex="-1" aria-label="Hidden input for typeahead">
          <input type="text" autocomplete="off" autocorrect="off" autocapitalize="off" spellcheck="false" class="js-input typeahead-input form-control border-0 box-shadow-none input-block width-full no-focus-indicator" aria-label="Command palette input" aria-haspopup="listbox" aria-expanded="false" aria-autocomplete="list" aria-controls="command-palette-page-stack" role="combobox" data-action="
              input:command-palette-input#onInput
              keydown:command-palette-input#onKeydown
            " placeholder="Search or jump to...">
        </div>
          <div data-view-component="true" class="position-relative d-inline-block">
    <button aria-keyshortcuts="Control+Backspace" data-action="click:command-palette-input#onClear keypress:command-palette-input#onClear" data-target="command-palette-input.clearButton" id="command-palette-clear-button" hidden="hidden" type="button" data-view-component="true" class="btn-octicon command-palette-input-clear-button" aria-labelledby="tooltip-3fa78715-44ee-431f-98b8-02ddd6bce2d0">      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x-circle-fill">
    <path fill-rule="evenodd" d="M2.343 13.657A8 8 0 1113.657 2.343 8 8 0 012.343 13.657zM6.03 4.97a.75.75 0 00-1.06 1.06L6.94 8 4.97 9.97a.75.75 0 101.06 1.06L8 9.06l1.97 1.97a.75.75 0 101.06-1.06L9.06 8l1.97-1.97a.75.75 0 10-1.06-1.06L8 6.94 6.03 4.97z"></path>
</svg>
</button>    <tool-tip id="tooltip-3fa78715-44ee-431f-98b8-02ddd6bce2d0" for="command-palette-clear-button" data-direction="w" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip">Clear Command Palette</tool-tip>
</div>
      </command-palette-input>

      <command-palette-page-stack data-default-scope-id="R_kgDOIhkTtA" data-default-scope-type="Repository" data-action="command-palette-page-octicons-cached:command-palette-page-stack#cacheOcticons" data-current-mode="" data-catalyst="" data-target="command-palette.pageStack" data-current-query-text="">
          <command-palette-tip class="color-fg-muted f6 px-3 py-1 my-2" data-scope-types="[&quot;&quot;,&quot;owner&quot;,&quot;repository&quot;]" data-mode="" data-value="" data-match-mode="" data-catalyst="" hidden="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type <kbd class="hx_kbd">#</kbd> to search pull requests
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip class="color-fg-muted f6 px-3 py-1 my-2" data-scope-types="[&quot;&quot;,&quot;owner&quot;,&quot;repository&quot;]" data-mode="" data-value="" data-match-mode="" data-catalyst="" hidden="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type <kbd class="hx_kbd">#</kbd> to search issues
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip class="color-fg-muted f6 px-3 py-1 my-2" data-scope-types="[&quot;owner&quot;,&quot;repository&quot;]" data-mode="" data-value="" data-match-mode="" data-catalyst="" hidden="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type <kbd class="hx_kbd">#</kbd> to search discussions
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip class="color-fg-muted f6 px-3 py-1 my-2" data-scope-types="[&quot;owner&quot;,&quot;repository&quot;]" data-mode="" data-value="" data-match-mode="" data-catalyst="" hidden="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type <kbd class="hx_kbd">!</kbd> to search projects
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip class="color-fg-muted f6 px-3 py-1 my-2" data-scope-types="[&quot;owner&quot;]" data-mode="" data-value="" data-match-mode="" data-catalyst="" hidden="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type <kbd class="hx_kbd">@</kbd> to search teams
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip class="color-fg-muted f6 px-3 py-1 my-2" data-scope-types="[&quot;&quot;]" data-mode="" data-value="" data-match-mode="" data-catalyst="" hidden="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type <kbd class="hx_kbd">@</kbd> to search people and organizations
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip class="color-fg-muted f6 px-3 py-1 my-2" data-scope-types="[&quot;&quot;,&quot;owner&quot;,&quot;repository&quot;]" data-mode="" data-value="" data-match-mode="" data-catalyst="" hidden="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type <kbd class="hx_kbd">&gt;</kbd> to activate command mode
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip class="color-fg-muted f6 px-3 py-1 my-2" data-scope-types="[&quot;&quot;,&quot;owner&quot;,&quot;repository&quot;]" data-mode="" data-value="" data-match-mode="" data-catalyst="" hidden="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Go to your accessibility settings to change your keyboard shortcuts
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip class="color-fg-muted f6 px-3 py-1 my-2" data-scope-types="[&quot;&quot;,&quot;owner&quot;,&quot;repository&quot;]" data-mode="#" data-value="" data-match-mode="" data-catalyst="" hidden="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type author:@me to search your content
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip class="color-fg-muted f6 px-3 py-1 my-2" data-scope-types="[&quot;&quot;,&quot;owner&quot;,&quot;repository&quot;]" data-mode="#" data-value="" data-match-mode="" data-catalyst="" hidden="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type is:pr to filter to pull requests
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip class="color-fg-muted f6 px-3 py-1 my-2" data-scope-types="[&quot;&quot;,&quot;owner&quot;,&quot;repository&quot;]" data-mode="#" data-value="" data-match-mode="" data-catalyst="" hidden="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type is:issue to filter to issues
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip class="color-fg-muted f6 px-3 py-1 my-2" data-scope-types="[&quot;owner&quot;,&quot;repository&quot;]" data-mode="#" data-value="" data-match-mode="" data-catalyst="" hidden="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type is:project to filter to projects
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip class="color-fg-muted f6 px-3 py-1 my-2" data-scope-types="[&quot;&quot;,&quot;owner&quot;,&quot;repository&quot;]" data-mode="#" data-value="" data-match-mode="" data-catalyst="" hidden="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type is:open to filter to open content
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
        <command-palette-tip class="mx-3 my-2 flash flash-error d-flex flex-items-center" data-scope-types="*" data-on-error="" data-mode="*" data-catalyst="" hidden="" data-match-mode="" data-value="*">
          <div>
            <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert">
    <path fill-rule="evenodd" d="M8.22 1.754a.25.25 0 00-.44 0L1.698 13.132a.25.25 0 00.22.368h12.164a.25.25 0 00.22-.368L8.22 1.754zm-1.763-.707c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0114.082 15H1.918a1.75 1.75 0 01-1.543-2.575L6.457 1.047zM9 11a1 1 0 11-2 0 1 1 0 012 0zm-.25-5.25a.75.75 0 00-1.5 0v2.5a.75.75 0 001.5 0v-2.5z"></path>
</svg>
          </div>
          <div class="px-2">
            We’ve encountered an error and some results aren't available at this time. Type a new search or try again later.
          </div>
        </command-palette-tip>
        <command-palette-tip class="h4 color-fg-default pl-3 pb-2 pt-3" data-on-empty="" data-scope-types="*" data-match-mode="[^?]|^$" data-mode="*" data-catalyst="" hidden="" data-value="*">
          No results matched your search
        </command-palette-tip>

        <div hidden="">

            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="arrow-right-color-fg-muted">
              <svg height="16" class="octicon octicon-arrow-right color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.22 2.97a.75.75 0 011.06 0l4.25 4.25a.75.75 0 010 1.06l-4.25 4.25a.75.75 0 01-1.06-1.06l2.97-2.97H3.75a.75.75 0 010-1.5h7.44L8.22 4.03a.75.75 0 010-1.06z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="arrow-right-color-fg-default">
              <svg height="16" class="octicon octicon-arrow-right color-fg-default" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.22 2.97a.75.75 0 011.06 0l4.25 4.25a.75.75 0 010 1.06l-4.25 4.25a.75.75 0 01-1.06-1.06l2.97-2.97H3.75a.75.75 0 010-1.5h7.44L8.22 4.03a.75.75 0 010-1.06z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="codespaces-color-fg-muted">
              <svg height="16" class="octicon octicon-codespaces color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M2 1.75C2 .784 2.784 0 3.75 0h8.5C13.216 0 14 .784 14 1.75v5a1.75 1.75 0 01-1.75 1.75h-8.5A1.75 1.75 0 012 6.75v-5zm1.75-.25a.25.25 0 00-.25.25v5c0 .138.112.25.25.25h8.5a.25.25 0 00.25-.25v-5a.25.25 0 00-.25-.25h-8.5zM0 11.25c0-.966.784-1.75 1.75-1.75h12.5c.966 0 1.75.784 1.75 1.75v3A1.75 1.75 0 0114.25 16H1.75A1.75 1.75 0 010 14.25v-3zM1.75 11a.25.25 0 00-.25.25v3c0 .138.112.25.25.25h12.5a.25.25 0 00.25-.25v-3a.25.25 0 00-.25-.25H1.75z"></path><path fill-rule="evenodd" d="M3 12.75a.75.75 0 01.75-.75h.5a.75.75 0 010 1.5h-.5a.75.75 0 01-.75-.75zm4 0a.75.75 0 01.75-.75h4.5a.75.75 0 010 1.5h-4.5a.75.75 0 01-.75-.75z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="copy-color-fg-muted">
              <svg height="16" class="octicon octicon-copy color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 010 1.5h-1.5a.25.25 0 00-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 00.25-.25v-1.5a.75.75 0 011.5 0v1.5A1.75 1.75 0 019.25 16h-7.5A1.75 1.75 0 010 14.25v-7.5z"></path><path fill-rule="evenodd" d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0114.25 11h-7.5A1.75 1.75 0 015 9.25v-7.5zm1.75-.25a.25.25 0 00-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 00.25-.25v-7.5a.25.25 0 00-.25-.25h-7.5z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="dash-color-fg-muted">
              <svg height="16" class="octicon octicon-dash color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M2 7.75A.75.75 0 012.75 7h10a.75.75 0 010 1.5h-10A.75.75 0 012 7.75z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="file-color-fg-muted">
              <svg height="16" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M3.75 1.5a.25.25 0 00-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 00.25-.25V6h-2.75A1.75 1.75 0 019 4.25V1.5H3.75zm6.75.062V4.25c0 .138.112.25.25.25h2.688a.252.252 0 00-.011-.013l-2.914-2.914a.272.272 0 00-.013-.011zM2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0113.25 16h-9.5A1.75 1.75 0 012 14.25V1.75z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="gear-color-fg-muted">
              <svg height="16" class="octicon octicon-gear color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.429 1.525a6.593 6.593 0 011.142 0c.036.003.108.036.137.146l.289 1.105c.147.56.55.967.997 1.189.174.086.341.183.501.29.417.278.97.423 1.53.27l1.102-.303c.11-.03.175.016.195.046.219.31.41.641.573.989.014.031.022.11-.059.19l-.815.806c-.411.406-.562.957-.53 1.456a4.588 4.588 0 010 .582c-.032.499.119 1.05.53 1.456l.815.806c.08.08.073.159.059.19a6.494 6.494 0 01-.573.99c-.02.029-.086.074-.195.045l-1.103-.303c-.559-.153-1.112-.008-1.529.27-.16.107-.327.204-.5.29-.449.222-.851.628-.998 1.189l-.289 1.105c-.029.11-.101.143-.137.146a6.613 6.613 0 01-1.142 0c-.036-.003-.108-.037-.137-.146l-.289-1.105c-.147-.56-.55-.967-.997-1.189a4.502 4.502 0 01-.501-.29c-.417-.278-.97-.423-1.53-.27l-1.102.303c-.11.03-.175-.016-.195-.046a6.492 6.492 0 01-.573-.989c-.014-.031-.022-.11.059-.19l.815-.806c.411-.406.562-.957.53-1.456a4.587 4.587 0 010-.582c.032-.499-.119-1.05-.53-1.456l-.815-.806c-.08-.08-.073-.159-.059-.19a6.44 6.44 0 01.573-.99c.02-.029.086-.075.195-.045l1.103.303c.559.153 1.112.008 1.529-.27.16-.107.327-.204.5-.29.449-.222.851-.628.998-1.189l.289-1.105c.029-.11.101-.143.137-.146zM8 0c-.236 0-.47.01-.701.03-.743.065-1.29.615-1.458 1.261l-.29 1.106c-.017.066-.078.158-.211.224a5.994 5.994 0 00-.668.386c-.123.082-.233.09-.3.071L3.27 2.776c-.644-.177-1.392.02-1.82.63a7.977 7.977 0 00-.704 1.217c-.315.675-.111 1.422.363 1.891l.815.806c.05.048.098.147.088.294a6.084 6.084 0 000 .772c.01.147-.038.246-.088.294l-.815.806c-.474.469-.678 1.216-.363 1.891.2.428.436.835.704 1.218.428.609 1.176.806 1.82.63l1.103-.303c.066-.019.176-.011.299.071.213.143.436.272.668.386.133.066.194.158.212.224l.289 1.106c.169.646.715 1.196 1.458 1.26a8.094 8.094 0 001.402 0c.743-.064 1.29-.614 1.458-1.26l.29-1.106c.017-.066.078-.158.211-.224a5.98 5.98 0 00.668-.386c.123-.082.233-.09.3-.071l1.102.302c.644.177 1.392-.02 1.82-.63.268-.382.505-.789.704-1.217.315-.675.111-1.422-.364-1.891l-.814-.806c-.05-.048-.098-.147-.088-.294a6.1 6.1 0 000-.772c-.01-.147.039-.246.088-.294l.814-.806c.475-.469.679-1.216.364-1.891a7.992 7.992 0 00-.704-1.218c-.428-.609-1.176-.806-1.82-.63l-1.103.303c-.066.019-.176.011-.299-.071a5.991 5.991 0 00-.668-.386c-.133-.066-.194-.158-.212-.224L10.16 1.29C9.99.645 9.444.095 8.701.031A8.094 8.094 0 008 0zm1.5 8a1.5 1.5 0 11-3 0 1.5 1.5 0 013 0zM11 8a3 3 0 11-6 0 3 3 0 016 0z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="lock-color-fg-muted">
              <svg height="16" class="octicon octicon-lock color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 4v2h-.25A1.75 1.75 0 002 7.75v5.5c0 .966.784 1.75 1.75 1.75h8.5A1.75 1.75 0 0014 13.25v-5.5A1.75 1.75 0 0012.25 6H12V4a4 4 0 10-8 0zm6.5 2V4a2.5 2.5 0 00-5 0v2h5zM12 7.5h.25a.25.25 0 01.25.25v5.5a.25.25 0 01-.25.25h-8.5a.25.25 0 01-.25-.25v-5.5a.25.25 0 01.25-.25H12z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="moon-color-fg-muted">
              <svg height="16" class="octicon octicon-moon color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M9.598 1.591a.75.75 0 01.785-.175 7 7 0 11-8.967 8.967.75.75 0 01.961-.96 5.5 5.5 0 007.046-7.046.75.75 0 01.175-.786zm1.616 1.945a7 7 0 01-7.678 7.678 5.5 5.5 0 107.678-7.678z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="person-color-fg-muted">
              <svg height="16" class="octicon octicon-person color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M10.5 5a2.5 2.5 0 11-5 0 2.5 2.5 0 015 0zm.061 3.073a4 4 0 10-5.123 0 6.004 6.004 0 00-3.431 5.142.75.75 0 001.498.07 4.5 4.5 0 018.99 0 .75.75 0 101.498-.07 6.005 6.005 0 00-3.432-5.142z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="pencil-color-fg-muted">
              <svg height="16" class="octicon octicon-pencil color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M11.013 1.427a1.75 1.75 0 012.474 0l1.086 1.086a1.75 1.75 0 010 2.474l-8.61 8.61c-.21.21-.47.364-.756.445l-3.251.93a.75.75 0 01-.927-.928l.929-3.25a1.75 1.75 0 01.445-.758l8.61-8.61zm1.414 1.06a.25.25 0 00-.354 0L10.811 3.75l1.439 1.44 1.263-1.263a.25.25 0 000-.354l-1.086-1.086zM11.189 6.25L9.75 4.81l-6.286 6.287a.25.25 0 00-.064.108l-.558 1.953 1.953-.558a.249.249 0 00.108-.064l6.286-6.286z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="issue-opened-open">
              <svg height="16" class="octicon octicon-issue-opened open" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M8 9.5a1.5 1.5 0 100-3 1.5 1.5 0 000 3z"></path><path fill-rule="evenodd" d="M8 0a8 8 0 100 16A8 8 0 008 0zM1.5 8a6.5 6.5 0 1113 0 6.5 6.5 0 01-13 0z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="git-pull-request-draft-color-fg-muted">
              <svg height="16" class="octicon octicon-git-pull-request-draft color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M2.5 3.25a.75.75 0 111.5 0 .75.75 0 01-1.5 0zM3.25 1a2.25 2.25 0 00-.75 4.372v5.256a2.251 2.251 0 101.5 0V5.372A2.25 2.25 0 003.25 1zm0 11a.75.75 0 100 1.5.75.75 0 000-1.5zm9.5 3a2.25 2.25 0 100-4.5 2.25 2.25 0 000 4.5zm0-3a.75.75 0 100 1.5.75.75 0 000-1.5z"></path><path d="M14 7.5a1.25 1.25 0 11-2.5 0 1.25 1.25 0 012.5 0zm0-4.25a1.25 1.25 0 11-2.5 0 1.25 1.25 0 012.5 0z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="search-color-fg-muted">
              <svg height="16" class="octicon octicon-search color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M11.5 7a4.499 4.499 0 11-8.998 0A4.499 4.499 0 0111.5 7zm-.82 4.74a6 6 0 111.06-1.06l3.04 3.04a.75.75 0 11-1.06 1.06l-3.04-3.04z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="sun-color-fg-muted">
              <svg height="16" class="octicon octicon-sun color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 10.5a2.5 2.5 0 100-5 2.5 2.5 0 000 5zM8 12a4 4 0 100-8 4 4 0 000 8zM8 0a.75.75 0 01.75.75v1.5a.75.75 0 01-1.5 0V.75A.75.75 0 018 0zm0 13a.75.75 0 01.75.75v1.5a.75.75 0 01-1.5 0v-1.5A.75.75 0 018 13zM2.343 2.343a.75.75 0 011.061 0l1.06 1.061a.75.75 0 01-1.06 1.06l-1.06-1.06a.75.75 0 010-1.06zm9.193 9.193a.75.75 0 011.06 0l1.061 1.06a.75.75 0 01-1.06 1.061l-1.061-1.06a.75.75 0 010-1.061zM16 8a.75.75 0 01-.75.75h-1.5a.75.75 0 010-1.5h1.5A.75.75 0 0116 8zM3 8a.75.75 0 01-.75.75H.75a.75.75 0 010-1.5h1.5A.75.75 0 013 8zm10.657-5.657a.75.75 0 010 1.061l-1.061 1.06a.75.75 0 11-1.06-1.06l1.06-1.06a.75.75 0 011.06 0zm-9.193 9.193a.75.75 0 010 1.06l-1.06 1.061a.75.75 0 11-1.061-1.06l1.06-1.061a.75.75 0 011.061 0z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="sync-color-fg-muted">
              <svg height="16" class="octicon octicon-sync color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 2.5a5.487 5.487 0 00-4.131 1.869l1.204 1.204A.25.25 0 014.896 6H1.25A.25.25 0 011 5.75V2.104a.25.25 0 01.427-.177l1.38 1.38A7.001 7.001 0 0114.95 7.16a.75.75 0 11-1.49.178A5.501 5.501 0 008 2.5zM1.705 8.005a.75.75 0 01.834.656 5.501 5.501 0 009.592 2.97l-1.204-1.204a.25.25 0 01.177-.427h3.646a.25.25 0 01.25.25v3.646a.25.25 0 01-.427.177l-1.38-1.38A7.001 7.001 0 011.05 8.84a.75.75 0 01.656-.834z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="trash-color-fg-muted">
              <svg height="16" class="octicon octicon-trash color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M6.5 1.75a.25.25 0 01.25-.25h2.5a.25.25 0 01.25.25V3h-3V1.75zm4.5 0V3h2.25a.75.75 0 010 1.5H2.75a.75.75 0 010-1.5H5V1.75C5 .784 5.784 0 6.75 0h2.5C10.216 0 11 .784 11 1.75zM4.496 6.675a.75.75 0 10-1.492.15l.66 6.6A1.75 1.75 0 005.405 15h5.19c.9 0 1.652-.681 1.741-1.576l.66-6.6a.75.75 0 00-1.492-.149l-.66 6.6a.25.25 0 01-.249.225h-5.19a.25.25 0 01-.249-.225l-.66-6.6z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="key-color-fg-muted">
              <svg height="16" class="octicon octicon-key color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M6.5 5.5a4 4 0 112.731 3.795.75.75 0 00-.768.18L7.44 10.5H6.25a.75.75 0 00-.75.75v1.19l-.06.06H4.25a.75.75 0 00-.75.75v1.19l-.06.06H1.75a.25.25 0 01-.25-.25v-1.69l5.024-5.023a.75.75 0 00.181-.768A3.995 3.995 0 016.5 5.5zm4-5.5a5.5 5.5 0 00-5.348 6.788L.22 11.72a.75.75 0 00-.22.53v2C0 15.216.784 16 1.75 16h2a.75.75 0 00.53-.22l.5-.5a.75.75 0 00.22-.53V14h.75a.75.75 0 00.53-.22l.5-.5a.75.75 0 00.22-.53V12h.75a.75.75 0 00.53-.22l.932-.932A5.5 5.5 0 1010.5 0zm.5 6a1 1 0 100-2 1 1 0 000 2z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="comment-discussion-color-fg-muted">
              <svg height="16" class="octicon octicon-comment-discussion color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M1.5 2.75a.25.25 0 01.25-.25h8.5a.25.25 0 01.25.25v5.5a.25.25 0 01-.25.25h-3.5a.75.75 0 00-.53.22L3.5 11.44V9.25a.75.75 0 00-.75-.75h-1a.25.25 0 01-.25-.25v-5.5zM1.75 1A1.75 1.75 0 000 2.75v5.5C0 9.216.784 10 1.75 10H2v1.543a1.457 1.457 0 002.487 1.03L7.061 10h3.189A1.75 1.75 0 0012 8.25v-5.5A1.75 1.75 0 0010.25 1h-8.5zM14.5 4.75a.25.25 0 00-.25-.25h-.5a.75.75 0 110-1.5h.5c.966 0 1.75.784 1.75 1.75v5.5A1.75 1.75 0 0114.25 12H14v1.543a1.457 1.457 0 01-2.487 1.03L9.22 12.28a.75.75 0 111.06-1.06l2.22 2.22v-2.19a.75.75 0 01.75-.75h1a.25.25 0 00.25-.25v-5.5z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="bell-color-fg-muted">
              <svg height="16" class="octicon octicon-bell color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M8 16a2 2 0 001.985-1.75c.017-.137-.097-.25-.235-.25h-3.5c-.138 0-.252.113-.235.25A2 2 0 008 16z"></path><path fill-rule="evenodd" d="M8 1.5A3.5 3.5 0 004.5 5v2.947c0 .346-.102.683-.294.97l-1.703 2.556a.018.018 0 00-.003.01l.001.006c0 .002.002.004.004.006a.017.017 0 00.006.004l.007.001h10.964l.007-.001a.016.016 0 00.006-.004.016.016 0 00.004-.006l.001-.007a.017.017 0 00-.003-.01l-1.703-2.554a1.75 1.75 0 01-.294-.97V5A3.5 3.5 0 008 1.5zM3 5a5 5 0 0110 0v2.947c0 .05.015.098.042.139l1.703 2.555A1.518 1.518 0 0113.482 13H2.518a1.518 1.518 0 01-1.263-2.36l1.703-2.554A.25.25 0 003 7.947V5z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="bell-slash-color-fg-muted">
              <svg height="16" class="octicon octicon-bell-slash color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 1.5c-.997 0-1.895.416-2.534 1.086A.75.75 0 014.38 1.55 5 5 0 0113 5v2.373a.75.75 0 01-1.5 0V5A3.5 3.5 0 008 1.5zM4.182 4.31L1.19 2.143a.75.75 0 10-.88 1.214L3 5.305v2.642a.25.25 0 01-.042.139L1.255 10.64A1.518 1.518 0 002.518 13h11.108l1.184.857a.75.75 0 10.88-1.214l-1.375-.996a1.196 1.196 0 00-.013-.01L4.198 4.321a.733.733 0 00-.016-.011zm7.373 7.19L4.5 6.391v1.556c0 .346-.102.683-.294.97l-1.703 2.556a.018.018 0 00-.003.01.015.015 0 00.005.012.017.017 0 00.006.004l.007.001h9.037zM8 16a2 2 0 001.985-1.75c.017-.137-.097-.25-.235-.25h-3.5c-.138 0-.252.113-.235.25A2 2 0 008 16z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="paintbrush-color-fg-muted">
              <svg height="16" class="octicon octicon-paintbrush color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M11.134 1.535C9.722 2.562 8.16 4.057 6.889 5.312 5.8 6.387 5.041 7.401 4.575 8.294a3.745 3.745 0 00-3.227 1.054c-.43.431-.69 1.066-.86 1.657a11.982 11.982 0 00-.358 1.914A21.263 21.263 0 000 15.203v.054l.75-.007-.007.75h.054a14.404 14.404 0 00.654-.012 21.243 21.243 0 001.63-.118c.62-.07 1.3-.18 1.914-.357.592-.17 1.226-.43 1.657-.861a3.745 3.745 0 001.055-3.217c.908-.461 1.942-1.216 3.04-2.3 1.279-1.262 2.764-2.825 3.775-4.249.501-.706.923-1.428 1.125-2.096.2-.659.235-1.469-.368-2.07-.606-.607-1.42-.55-2.069-.34-.66.213-1.376.646-2.076 1.155zm-3.95 8.48a3.76 3.76 0 00-1.19-1.192 9.758 9.758 0 011.161-1.607l1.658 1.658a9.853 9.853 0 01-1.63 1.142zM.742 16l.007-.75-.75.008A.75.75 0 00.743 16zM12.016 2.749c-1.224.89-2.605 2.189-3.822 3.384l1.718 1.718c1.21-1.205 2.51-2.597 3.387-3.833.47-.662.78-1.227.912-1.662.134-.444.032-.551.009-.575h-.001V1.78c-.014-.014-.112-.113-.548.027-.432.14-.995.462-1.655.942zM1.62 13.089a19.56 19.56 0 00-.104 1.395 19.55 19.55 0 001.396-.104 10.528 10.528 0 001.668-.309c.526-.151.856-.325 1.011-.48a2.25 2.25 0 00-3.182-3.182c-.155.155-.329.485-.48 1.01a10.515 10.515 0 00-.309 1.67z"></path></svg>
            </div>

            <command-palette-item-group data-group-id="top" data-group-title="Top result" data-group-hint="" data-group-limits="{}" data-default-priority="0" data-catalyst="" class="py-2 border-top" hidden="true" data-skip-template="">
            
          <div class="d-flex flex-justify-between my-2 px-3">
            <span data-target="command-palette-item-group.header" class="color-fg-muted text-bold f6 text-normal">
              Top result
            </span>
            <span data-target="command-palette-item-group.header" class="color-fg-muted f6 text-normal">
              
            </span>
          </div>
          <div role="listbox" class="list-style-none" data-target="command-palette-item-group.list" aria-label="Top result results"></div>
        </command-palette-item-group>
            <command-palette-item-group data-group-id="commands" data-group-title="Commands" data-group-hint="Type &gt; to filter" data-group-limits="{&quot;static_items_page&quot;:50,&quot;issue&quot;:50,&quot;pull_request&quot;:50,&quot;discussion&quot;:50}" data-default-priority="1" data-catalyst="" class="py-2 border-top" hidden="true" data-skip-template="">
            
          <div class="d-flex flex-justify-between my-2 px-3">
            <span data-target="command-palette-item-group.header" class="color-fg-muted text-bold f6 text-normal">
              Commands
            </span>
            <span data-target="command-palette-item-group.header" class="color-fg-muted f6 text-normal">
              Type &gt; to filter
            </span>
          </div>
          <div role="listbox" class="list-style-none" data-target="command-palette-item-group.list" aria-label="Commands results"></div>
        </command-palette-item-group>
            <command-palette-item-group data-group-id="global_commands" data-group-title="Global Commands" data-group-hint="Type &gt; to filter" data-group-limits="{&quot;issue&quot;:0,&quot;pull_request&quot;:0,&quot;discussion&quot;:0}" data-default-priority="2" data-catalyst="" class="py-2 border-top" hidden="true" data-skip-template="">
            
          <div class="d-flex flex-justify-between my-2 px-3">
            <span data-target="command-palette-item-group.header" class="color-fg-muted text-bold f6 text-normal">
              Global Commands
            </span>
            <span data-target="command-palette-item-group.header" class="color-fg-muted f6 text-normal">
              Type &gt; to filter
            </span>
          </div>
          <div role="listbox" class="list-style-none" data-target="command-palette-item-group.list" aria-label="Global Commands results"></div>
        </command-palette-item-group>
            <command-palette-item-group data-group-id="this_page" data-group-title="This Page" data-group-hint="" data-group-limits="{}" data-default-priority="3" data-catalyst="" class="py-2 border-top" hidden="true" data-skip-template="">
            
          <div class="d-flex flex-justify-between my-2 px-3">
            <span data-target="command-palette-item-group.header" class="color-fg-muted text-bold f6 text-normal">
              This Page
            </span>
            <span data-target="command-palette-item-group.header" class="color-fg-muted f6 text-normal">
              
            </span>
          </div>
          <div role="listbox" class="list-style-none" data-target="command-palette-item-group.list" aria-label="This Page results"></div>
        </command-palette-item-group>
            <command-palette-item-group data-group-id="files" data-group-title="Files" data-group-hint="" data-group-limits="{}" data-default-priority="4" data-catalyst="" class="py-2 border-top" hidden="true" data-skip-template="">
            
          <div class="d-flex flex-justify-between my-2 px-3">
            <span data-target="command-palette-item-group.header" class="color-fg-muted text-bold f6 text-normal">
              Files
            </span>
            <span data-target="command-palette-item-group.header" class="color-fg-muted f6 text-normal">
              
            </span>
          </div>
          <div role="listbox" class="list-style-none" data-target="command-palette-item-group.list" aria-label="Files results"></div>
        </command-palette-item-group>
            <command-palette-item-group data-group-id="default" data-group-title="Default" data-group-hint="" data-group-limits="{&quot;static_items_page&quot;:50}" data-default-priority="5" data-catalyst="" class="py-2 border-top" hidden="true" data-skip-template="">
            
          <div role="listbox" class="list-style-none" data-target="command-palette-item-group.list" aria-label="Default results"></div>
        </command-palette-item-group>
            <command-palette-item-group data-group-id="pages" data-group-title="Pages" data-group-hint="" data-group-limits="{&quot;repository&quot;:10}" data-default-priority="6" data-catalyst="" class="py-2 border-top" hidden="true" data-skip-template="">
            
          <div class="d-flex flex-justify-between my-2 px-3">
            <span data-target="command-palette-item-group.header" class="color-fg-muted text-bold f6 text-normal">
              Pages
            </span>
            <span data-target="command-palette-item-group.header" class="color-fg-muted f6 text-normal">
              
            </span>
          </div>
          <div role="listbox" class="list-style-none" data-target="command-palette-item-group.list" aria-label="Pages results"></div>
        </command-palette-item-group>
            <command-palette-item-group data-group-id="access_policies" data-group-title="Access Policies" data-group-hint="" data-group-limits="{}" data-default-priority="7" data-catalyst="" class="py-2 border-top" hidden="true" data-skip-template="">
            
          <div class="d-flex flex-justify-between my-2 px-3">
            <span data-target="command-palette-item-group.header" class="color-fg-muted text-bold f6 text-normal">
              Access Policies
            </span>
            <span data-target="command-palette-item-group.header" class="color-fg-muted f6 text-normal">
              
            </span>
          </div>
          <div role="listbox" class="list-style-none" data-target="command-palette-item-group.list" aria-label="Access Policies results"></div>
        </command-palette-item-group>
            <command-palette-item-group data-group-id="organizations" data-group-title="Organizations" data-group-hint="" data-group-limits="{}" data-default-priority="8" data-catalyst="" class="py-2 border-top" hidden="true" data-skip-template="">
            
          <div class="d-flex flex-justify-between my-2 px-3">
            <span data-target="command-palette-item-group.header" class="color-fg-muted text-bold f6 text-normal">
              Organizations
            </span>
            <span data-target="command-palette-item-group.header" class="color-fg-muted f6 text-normal">
              
            </span>
          </div>
          <div role="listbox" class="list-style-none" data-target="command-palette-item-group.list" aria-label="Organizations results"></div>
        </command-palette-item-group>
            <command-palette-item-group data-group-id="repositories" data-group-title="Repositories" data-group-hint="" data-group-limits="{}" data-default-priority="9" data-catalyst="" class="py-2 border-top" hidden="true" data-skip-template="">
            
          <div class="d-flex flex-justify-between my-2 px-3">
            <span data-target="command-palette-item-group.header" class="color-fg-muted text-bold f6 text-normal">
              Repositories
            </span>
            <span data-target="command-palette-item-group.header" class="color-fg-muted f6 text-normal">
              
            </span>
          </div>
          <div role="listbox" class="list-style-none" data-target="command-palette-item-group.list" aria-label="Repositories results"></div>
        </command-palette-item-group>
            <command-palette-item-group data-group-id="references" data-group-title="Issues, pull requests, and discussions" data-group-hint="Type # to filter" data-group-limits="{}" data-default-priority="10" data-catalyst="" class="py-2 border-top" hidden="true" data-skip-template="">
            
          <div class="d-flex flex-justify-between my-2 px-3">
            <span data-target="command-palette-item-group.header" class="color-fg-muted text-bold f6 text-normal">
              Issues, pull requests, and discussions
            </span>
            <span data-target="command-palette-item-group.header" class="color-fg-muted f6 text-normal">
              Type # to filter
            </span>
          </div>
          <div role="listbox" class="list-style-none" data-target="command-palette-item-group.list" aria-label="Issues, pull requests, and discussions results"></div>
        </command-palette-item-group>
            <command-palette-item-group data-group-id="teams" data-group-title="Teams" data-group-hint="" data-group-limits="{}" data-default-priority="11" data-catalyst="" class="py-2 border-top" hidden="true" data-skip-template="">
            
          <div class="d-flex flex-justify-between my-2 px-3">
            <span data-target="command-palette-item-group.header" class="color-fg-muted text-bold f6 text-normal">
              Teams
            </span>
            <span data-target="command-palette-item-group.header" class="color-fg-muted f6 text-normal">
              
            </span>
          </div>
          <div role="listbox" class="list-style-none" data-target="command-palette-item-group.list" aria-label="Teams results"></div>
        </command-palette-item-group>
            <command-palette-item-group data-group-id="users" data-group-title="Users" data-group-hint="" data-group-limits="{}" data-default-priority="12" data-catalyst="" class="py-2 border-top" hidden="true" data-skip-template="">
            
          <div class="d-flex flex-justify-between my-2 px-3">
            <span data-target="command-palette-item-group.header" class="color-fg-muted text-bold f6 text-normal">
              Users
            </span>
            <span data-target="command-palette-item-group.header" class="color-fg-muted f6 text-normal">
              
            </span>
          </div>
          <div role="listbox" class="list-style-none" data-target="command-palette-item-group.list" aria-label="Users results"></div>
        </command-palette-item-group>
            <command-palette-item-group data-group-id="projects" data-group-title="Projects" data-group-hint="" data-group-limits="{}" data-default-priority="13" data-catalyst="" class="py-2 border-top" hidden="true" data-skip-template="">
            
          <div class="d-flex flex-justify-between my-2 px-3">
            <span data-target="command-palette-item-group.header" class="color-fg-muted text-bold f6 text-normal">
              Projects
            </span>
            <span data-target="command-palette-item-group.header" class="color-fg-muted f6 text-normal">
              
            </span>
          </div>
          <div role="listbox" class="list-style-none" data-target="command-palette-item-group.list" aria-label="Projects results"></div>
        </command-palette-item-group>
            <command-palette-item-group data-group-id="footer" data-group-title="Footer" data-group-hint="" data-group-limits="{}" data-default-priority="14" data-catalyst="" class="py-2 border-top" hidden="true" data-skip-template="">
            
          <div role="listbox" class="list-style-none" data-target="command-palette-item-group.list" aria-label="Footer results"></div>
        </command-palette-item-group>
            <command-palette-item-group data-group-id="modes_help" data-group-title="Modes" data-group-hint="" data-group-limits="{}" data-default-priority="15" data-catalyst="" class="py-2 border-top" hidden="true" data-skip-template="">
            
          <div class="d-flex flex-justify-between my-2 px-3">
            <span data-target="command-palette-item-group.header" class="color-fg-muted text-bold f6 text-normal">
              Modes
            </span>
            <span data-target="command-palette-item-group.header" class="color-fg-muted f6 text-normal">
              
            </span>
          </div>
          <div role="listbox" class="list-style-none" data-target="command-palette-item-group.list" aria-label="Modes results"></div>
        </command-palette-item-group>
            <command-palette-item-group data-group-id="filters_help" data-group-title="Use filters in issues, pull requests, discussions, and projects" data-group-hint="" data-group-limits="{}" data-default-priority="16" data-catalyst="" class="py-2 border-top" hidden="true" data-skip-template="">
            
          <div class="d-flex flex-justify-between my-2 px-3">
            <span data-target="command-palette-item-group.header" class="color-fg-muted text-bold f6 text-normal">
              Use filters in issues, pull requests, discussions, and projects
            </span>
            <span data-target="command-palette-item-group.header" class="color-fg-muted f6 text-normal">
              
            </span>
          </div>
          <div role="listbox" class="list-style-none" data-target="command-palette-item-group.list" aria-label="Use filters in issues, pull requests, discussions, and projects results"></div>
        </command-palette-item-group>

            <command-palette-page data-page-title="reyashv" data-scope-id="U_kgDOBdL8JQ" data-scope-type="owner" data-targets="command-palette-page-stack.defaultPages" hidden="" data-catalyst="" class="rounded-bottom-2 page-stack-transition-height" style="max-height:400px;">
            </command-palette-page>
            <command-palette-page data-page-title="python" data-scope-id="R_kgDOIhkTtA" data-scope-type="repository" data-targets="command-palette-page-stack.defaultPages" hidden="" data-catalyst="" class="rounded-bottom-2 page-stack-transition-height" style="max-height:400px;">
            </command-palette-page>
        </div>

        <command-palette-page data-is-root="" hidden="" data-page-title="" data-catalyst="" class="rounded-bottom-2 page-stack-transition-height" data-targets="command-palette-page-stack.pages" style="max-height:400px;" data-scope-id="" data-scope-type="">
        </command-palette-page>
          <command-palette-page data-page-title="reyashv" data-scope-id="U_kgDOBdL8JQ" data-scope-type="owner" hidden="" data-catalyst="" class="rounded-bottom-2 page-stack-transition-height" data-targets="command-palette-page-stack.pages" style="max-height:400px;">
          </command-palette-page>
          <command-palette-page data-page-title="python" data-scope-id="R_kgDOIhkTtA" data-scope-type="repository" hidden="" data-catalyst="" class="rounded-bottom-2 page-stack-transition-height" data-targets="command-palette-page-stack.pages" style="max-height:400px;">
          </command-palette-page>
      </command-palette-page-stack>

      <server-defined-provider data-type="search-links" data-targets="command-palette.serverDefinedProviderElements" data-supported-modes="" data-catalyst="" data-fetch-debounce="" data-supported-scope-types="" data-src="" data-supports-commands=""></server-defined-provider>
      <server-defined-provider data-type="help" data-targets="command-palette.serverDefinedProviderElements" data-supported-modes="" data-catalyst="" data-fetch-debounce="" data-supported-scope-types="" data-src="" data-supports-commands="">
          <command-palette-help data-group="modes_help" data-prefix="#" data-scope-types="[&quot;&quot;]" data-catalyst="" hidden="">
            <span data-target="command-palette-help.titleElement">Search for <strong>issues</strong> and <strong>pull requests</strong></span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd">#</kbd>
              </span>
          </command-palette-help>
          <command-palette-help data-group="modes_help" data-prefix="#" data-scope-types="[&quot;owner&quot;,&quot;repository&quot;]" data-catalyst="" hidden="">
            <span data-target="command-palette-help.titleElement">Search for <strong>issues, pull requests, discussions,</strong> and <strong>projects</strong></span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd">#</kbd>
              </span>
          </command-palette-help>
          <command-palette-help data-group="modes_help" data-prefix="@" data-scope-types="[&quot;&quot;]" data-catalyst="" hidden="">
            <span data-target="command-palette-help.titleElement">Search for <strong>organizations, repositories,</strong> and <strong>users</strong></span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd">@</kbd>
              </span>
          </command-palette-help>
          <command-palette-help data-group="modes_help" data-prefix="!" data-scope-types="[&quot;owner&quot;,&quot;repository&quot;]" data-catalyst="" hidden="">
            <span data-target="command-palette-help.titleElement">Search for <strong>projects</strong></span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd">!</kbd>
              </span>
          </command-palette-help>
          <command-palette-help data-group="modes_help" data-prefix="/" data-scope-types="[&quot;repository&quot;]" data-catalyst="" hidden="">
            <span data-target="command-palette-help.titleElement">Search for <strong>files</strong></span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd">/</kbd>
              </span>
          </command-palette-help>
          <command-palette-help data-group="modes_help" data-prefix="&gt;" data-scope-types="" data-catalyst="" hidden="">
            <span data-target="command-palette-help.titleElement">Activate <strong>command mode</strong></span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd">&gt;</kbd>
              </span>
          </command-palette-help>
          <command-palette-help data-group="filters_help" data-prefix="# author:@me" data-scope-types="" data-catalyst="" hidden="">
            <span data-target="command-palette-help.titleElement">Search your issues, pull requests, and discussions</span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd"># author:@me</kbd>
              </span>
          </command-palette-help>
          <command-palette-help data-group="filters_help" data-prefix="# author:@me" data-scope-types="" data-catalyst="" hidden="">
            <span data-target="command-palette-help.titleElement">Search your issues, pull requests, and discussions</span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd"># author:@me</kbd>
              </span>
          </command-palette-help>
          <command-palette-help data-group="filters_help" data-prefix="# is:pr" data-scope-types="" data-catalyst="" hidden="">
            <span data-target="command-palette-help.titleElement">Filter to pull requests</span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd"># is:pr</kbd>
              </span>
          </command-palette-help>
          <command-palette-help data-group="filters_help" data-prefix="# is:issue" data-scope-types="" data-catalyst="" hidden="">
            <span data-target="command-palette-help.titleElement">Filter to issues</span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd"># is:issue</kbd>
              </span>
          </command-palette-help>
          <command-palette-help data-group="filters_help" data-prefix="# is:discussion" data-scope-types="[&quot;owner&quot;,&quot;repository&quot;]" data-catalyst="" hidden="">
            <span data-target="command-palette-help.titleElement">Filter to discussions</span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd"># is:discussion</kbd>
              </span>
          </command-palette-help>
          <command-palette-help data-group="filters_help" data-prefix="# is:project" data-scope-types="[&quot;owner&quot;,&quot;repository&quot;]" data-catalyst="" hidden="">
            <span data-target="command-palette-help.titleElement">Filter to projects</span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd"># is:project</kbd>
              </span>
          </command-palette-help>
          <command-palette-help data-group="filters_help" data-prefix="# is:open" data-scope-types="" data-catalyst="" hidden="">
            <span data-target="command-palette-help.titleElement">Filter to open issues, pull requests, and discussions</span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd"># is:open</kbd>
              </span>
          </command-palette-help>
      </server-defined-provider>

        <server-defined-provider data-type="commands" data-fetch-debounce="0" data-src="/command_palette/commands" data-supported-modes="[]" data-supports-commands="" data-targets="command-palette.serverDefinedProviderElements" data-supported-scope-types="" data-catalyst=""></server-defined-provider>
        <server-defined-provider data-type="prefetched" data-fetch-debounce="0" data-src="/command_palette/jump_to_page_navigation" data-supported-modes="[&quot;&quot;]" data-supported-scope-types="[&quot;&quot;,&quot;owner&quot;,&quot;repository&quot;]" data-targets="command-palette.serverDefinedProviderElements" data-supports-commands="" data-catalyst=""></server-defined-provider>
        <server-defined-provider data-type="remote" data-fetch-debounce="200" data-src="/command_palette/issues" data-supported-modes="[&quot;#&quot;,&quot;#&quot;]" data-supported-scope-types="[&quot;owner&quot;,&quot;repository&quot;,&quot;&quot;]" data-targets="command-palette.serverDefinedProviderElements" data-supports-commands="" data-catalyst=""></server-defined-provider>
        <server-defined-provider data-type="remote" data-fetch-debounce="200" data-src="/command_palette/jump_to" data-supported-modes="[&quot;@&quot;,&quot;@&quot;]" data-supported-scope-types="[&quot;&quot;,&quot;owner&quot;]" data-targets="command-palette.serverDefinedProviderElements" data-supports-commands="" data-catalyst=""></server-defined-provider>
        <server-defined-provider data-type="remote" data-fetch-debounce="200" data-src="/command_palette/jump_to_members_only" data-supported-modes="[&quot;@&quot;,&quot;@&quot;,&quot;&quot;,&quot;&quot;]" data-supported-scope-types="[&quot;&quot;,&quot;owner&quot;]" data-targets="command-palette.serverDefinedProviderElements" data-supports-commands="" data-catalyst=""></server-defined-provider>
        <server-defined-provider data-type="prefetched" data-fetch-debounce="0" data-src="/command_palette/jump_to_members_only_prefetched" data-supported-modes="[&quot;@&quot;,&quot;@&quot;,&quot;&quot;,&quot;&quot;]" data-supported-scope-types="[&quot;&quot;,&quot;owner&quot;]" data-targets="command-palette.serverDefinedProviderElements" data-supports-commands="" data-catalyst=""></server-defined-provider>
        <server-defined-provider data-type="files" data-fetch-debounce="0" data-src="/command_palette/files" data-supported-modes="[&quot;/&quot;]" data-supported-scope-types="[&quot;repository&quot;]" data-targets="command-palette.serverDefinedProviderElements" data-supports-commands="" data-catalyst=""></server-defined-provider>
        <server-defined-provider data-type="remote" data-fetch-debounce="200" data-src="/command_palette/discussions" data-supported-modes="[&quot;#&quot;]" data-supported-scope-types="[&quot;owner&quot;,&quot;repository&quot;]" data-targets="command-palette.serverDefinedProviderElements" data-supports-commands="" data-catalyst=""></server-defined-provider>
        <server-defined-provider data-type="remote" data-fetch-debounce="200" data-src="/command_palette/projects" data-supported-modes="[&quot;#&quot;,&quot;!&quot;]" data-supported-scope-types="[&quot;owner&quot;,&quot;repository&quot;]" data-targets="command-palette.serverDefinedProviderElements" data-supports-commands="" data-catalyst=""></server-defined-provider>
        <server-defined-provider data-type="prefetched" data-fetch-debounce="0" data-src="/command_palette/recent_issues" data-supported-modes="[&quot;#&quot;,&quot;#&quot;]" data-supported-scope-types="[&quot;owner&quot;,&quot;repository&quot;,&quot;&quot;]" data-targets="command-palette.serverDefinedProviderElements" data-supports-commands="" data-catalyst=""></server-defined-provider>
        <server-defined-provider data-type="remote" data-fetch-debounce="200" data-src="/command_palette/teams" data-supported-modes="[&quot;@&quot;,&quot;&quot;]" data-supported-scope-types="[&quot;owner&quot;]" data-targets="command-palette.serverDefinedProviderElements" data-supports-commands="" data-catalyst=""></server-defined-provider>
        <server-defined-provider data-type="remote" data-fetch-debounce="200" data-src="/command_palette/name_with_owner_repository" data-supported-modes="[&quot;@&quot;,&quot;@&quot;,&quot;&quot;,&quot;&quot;]" data-supported-scope-types="[&quot;&quot;,&quot;owner&quot;]" data-targets="command-palette.serverDefinedProviderElements" data-supports-commands="" data-catalyst=""></server-defined-provider>
    <client-defined-provider data-catalyst="" data-provider-id="main-window-commands-provider" data-targets="command-palette.clientDefinedProviderElements"></client-defined-provider></command-palette>
  </details-dialog>
</details>

<div class="position-fixed bottom-0 left-0 ml-5 mb-5 js-command-palette-toasts" style="z-index: 1000">
  <div hidden="" class="Toast Toast--loading">
    <span class="Toast-icon">
      <svg class="Toast--spinner" viewBox="0 0 32 32" width="18" height="18" aria-hidden="true">
        <path fill="#959da5" d="M16 0 A16 16 0 0 0 16 32 A16 16 0 0 0 16 0 M16 4 A12 12 0 0 1 16 28 A12 12 0 0 1 16 4"></path>
        <path fill="#ffffff" d="M16 0 A16 16 0 0 1 32 16 L28 16 A12 12 0 0 0 16 4z"></path>
      </svg>
    </span>
    <span class="Toast-content"></span>
  </div>

  <div hidden="" class="anim-fade-in fast Toast Toast--error">
    <span class="Toast-icon">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-stop">
    <path fill-rule="evenodd" d="M4.47.22A.75.75 0 015 0h6a.75.75 0 01.53.22l4.25 4.25c.141.14.22.331.22.53v6a.75.75 0 01-.22.53l-4.25 4.25A.75.75 0 0111 16H5a.75.75 0 01-.53-.22L.22 11.53A.75.75 0 010 11V5a.75.75 0 01.22-.53L4.47.22zm.84 1.28L1.5 5.31v5.38l3.81 3.81h5.38l3.81-3.81V5.31L10.69 1.5H5.31zM8 4a.75.75 0 01.75.75v3.5a.75.75 0 01-1.5 0v-3.5A.75.75 0 018 4zm0 8a1 1 0 100-2 1 1 0 000 2z"></path>
</svg>
    </span>
    <span class="Toast-content"></span>
  </div>

  <div hidden="" class="anim-fade-in fast Toast Toast--warning">
    <span class="Toast-icon">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert">
    <path fill-rule="evenodd" d="M8.22 1.754a.25.25 0 00-.44 0L1.698 13.132a.25.25 0 00.22.368h12.164a.25.25 0 00.22-.368L8.22 1.754zm-1.763-.707c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0114.082 15H1.918a1.75 1.75 0 01-1.543-2.575L6.457 1.047zM9 11a1 1 0 11-2 0 1 1 0 012 0zm-.25-5.25a.75.75 0 00-1.5 0v2.5a.75.75 0 001.5 0v-2.5z"></path>
</svg>
    </span>
    <span class="Toast-content"></span>
  </div>


  <div hidden="" class="anim-fade-in fast Toast Toast--success">
    <span class="Toast-icon">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check">
    <path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"></path>
</svg>
    </span>
    <span class="Toast-content"></span>
  </div>

  <div hidden="" class="anim-fade-in fast Toast">
    <span class="Toast-icon">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-info">
    <path fill-rule="evenodd" d="M8 1.5a6.5 6.5 0 100 13 6.5 6.5 0 000-13zM0 8a8 8 0 1116 0A8 8 0 010 8zm6.5-.25A.75.75 0 017.25 7h1a.75.75 0 01.75.75v2.75h.25a.75.75 0 010 1.5h-2a.75.75 0 010-1.5h.25v-2h-.25a.75.75 0 01-.75-.75zM8 6a1 1 0 100-2 1 1 0 000 2z"></path>
</svg>
    </span>
    <span class="Toast-content"></span>
  </div>
</div>


  <div class="application-main " data-commit-hovercards-enabled="" data-discussion-hovercards-enabled="" data-issue-and-pr-hovercards-enabled="">
        <div itemscope="" itemtype="http://schema.org/SoftwareSourceCode" class="">
    <main id="js-repo-pjax-container">
      
  

<template class="js-user-list-create-dialog-template" data-label="Create list"></template>



    






  
  <div id="repository-container-header" class="pt-3 hide-full-screen" style="background-color: var(--color-page-header-bg);" data-turbo-replace="">

      <div class="d-flex flex-wrap flex-justify-end mb-3  px-3 px-md-4 px-lg-5" style="gap: 1rem;">

        <div class="flex-auto min-width-0 width-fit mr-3">
            
  <div class=" d-flex flex-wrap flex-items-center wb-break-word f3 text-normal">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-lock color-fg-muted mr-2">
    <path fill-rule="evenodd" d="M4 4v2h-.25A1.75 1.75 0 002 7.75v5.5c0 .966.784 1.75 1.75 1.75h8.5A1.75 1.75 0 0014 13.25v-5.5A1.75 1.75 0 0012.25 6H12V4a4 4 0 10-8 0zm6.5 2V4a2.5 2.5 0 00-5 0v2h5zM12 7.5h.25a.25.25 0 01.25.25v5.5a.25.25 0 01-.25.25h-8.5a.25.25 0 01-.25-.25v-5.5a.25.25 0 01.25-.25H12z"></path>
</svg>
    
    <span class="author flex-self-stretch" itemprop="author">
      <a class="url fn" rel="author" data-hovercard-type="user" data-hovercard-url="/users/reyashv/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/reyashv">
        reyashv
</a>    </span>
    <span class="mx-1 flex-self-stretch color-fg-muted">/</span>
    <strong itemprop="name" class="mr-2 flex-self-stretch">
      <a data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" href="https://github.com/reyashv/python">python</a>
    </strong>

    <span></span><span class="Label Label--secondary v-align-middle mr-1">Private</span>
  </div>


        </div>

          <ul class="pagehead-actions flex-shrink-0 d-none d-md-inline" style="padding: 2px 0;">

      

  <li>
          <notifications-list-subscription-form data-action="notifications-dialog-label-toggled:notifications-list-subscription-form#handleDialogLabelToggle" class="f5 position-relative" data-catalyst="">
      <details class="details-reset details-overlay f5 position-relative" data-target="notifications-list-subscription-form.details" data-action="toggle:notifications-list-subscription-form#detailsToggled">

        <summary data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;WATCH_BUTTON&quot;,&quot;repository_id&quot;:572068788,&quot;originating_url&quot;:&quot;https://github.com/reyashv/python&quot;,&quot;user_id&quot;:124596951}}" data-hydro-click-hmac="e14943801b599380db8116a136d0397f7356a6973731453f092199a5246a727b" data-ga-click="Repository, click Watch settings, action:files#disambiguate" aria-label="Notification settings" data-view-component="true" class="btn-sm btn" aria-haspopup="menu" role="button">    <span data-menu-button="">
            <span hidden="" data-target="notifications-list-subscription-form.unwatchButtonCopy">
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-eye">
    <path fill-rule="evenodd" d="M1.679 7.932c.412-.621 1.242-1.75 2.366-2.717C5.175 4.242 6.527 3.5 8 3.5c1.473 0 2.824.742 3.955 1.715 1.124.967 1.954 2.096 2.366 2.717a.119.119 0 010 .136c-.412.621-1.242 1.75-2.366 2.717C10.825 11.758 9.473 12.5 8 12.5c-1.473 0-2.824-.742-3.955-1.715C2.92 9.818 2.09 8.69 1.679 8.068a.119.119 0 010-.136zM8 2c-1.981 0-3.67.992-4.933 2.078C1.797 5.169.88 6.423.43 7.1a1.619 1.619 0 000 1.798c.45.678 1.367 1.932 2.637 3.024C4.329 13.008 6.019 14 8 14c1.981 0 3.67-.992 4.933-2.078 1.27-1.091 2.187-2.345 2.637-3.023a1.619 1.619 0 000-1.798c-.45-.678-1.367-1.932-2.637-3.023C11.671 2.992 9.981 2 8 2zm0 8a2 2 0 100-4 2 2 0 000 4z"></path>
</svg>
              Unwatch
            </span>
            <span hidden="" data-target="notifications-list-subscription-form.stopIgnoringButtonCopy">
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-bell-slash">
    <path fill-rule="evenodd" d="M8 1.5c-.997 0-1.895.416-2.534 1.086A.75.75 0 014.38 1.55 5 5 0 0113 5v2.373a.75.75 0 01-1.5 0V5A3.5 3.5 0 008 1.5zM4.182 4.31L1.19 2.143a.75.75 0 10-.88 1.214L3 5.305v2.642a.25.25 0 01-.042.139L1.255 10.64A1.518 1.518 0 002.518 13h11.108l1.184.857a.75.75 0 10.88-1.214l-1.375-.996a1.196 1.196 0 00-.013-.01L4.198 4.321a.733.733 0 00-.016-.011zm7.373 7.19L4.5 6.391v1.556c0 .346-.102.683-.294.97l-1.703 2.556a.018.018 0 00-.003.01.015.015 0 00.005.012.017.017 0 00.006.004l.007.001h9.037zM8 16a2 2 0 001.985-1.75c.017-.137-.097-.25-.235-.25h-3.5c-.138 0-.252.113-.235.25A2 2 0 008 16z"></path>
</svg>
              Stop ignoring
            </span>
            <span data-target="notifications-list-subscription-form.watchButtonCopy">
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-eye">
    <path fill-rule="evenodd" d="M1.679 7.932c.412-.621 1.242-1.75 2.366-2.717C5.175 4.242 6.527 3.5 8 3.5c1.473 0 2.824.742 3.955 1.715 1.124.967 1.954 2.096 2.366 2.717a.119.119 0 010 .136c-.412.621-1.242 1.75-2.366 2.717C10.825 11.758 9.473 12.5 8 12.5c-1.473 0-2.824-.742-3.955-1.715C2.92 9.818 2.09 8.69 1.679 8.068a.119.119 0 010-.136zM8 2c-1.981 0-3.67.992-4.933 2.078C1.797 5.169.88 6.423.43 7.1a1.619 1.619 0 000 1.798c.45.678 1.367 1.932 2.637 3.024C4.329 13.008 6.019 14 8 14c1.981 0 3.67-.992 4.933-2.078 1.27-1.091 2.187-2.345 2.637-3.023a1.619 1.619 0 000-1.798c-.45-.678-1.367-1.932-2.637-3.023C11.671 2.992 9.981 2 8 2zm0 8a2 2 0 100-4 2 2 0 000 4z"></path>
</svg>
              Watch
            </span>
          </span>
            <span id="repo-notifications-counter" data-target="notifications-list-subscription-form.socialCount" data-pjax-replace="true" data-turbo-replace="true" title="1" data-view-component="true" class="Counter">1</span>
          <span class="dropdown-caret"></span>
</summary>
        <details-menu class="SelectMenu  " role="menu" data-target="notifications-list-subscription-form.menu" data-focus-trap="suspended"><span class="sentinel" tabindex="0" aria-hidden="true"></span>
          <div class="SelectMenu-modal notifications-component-menu-modal">
            <header class="SelectMenu-header">
              <h3 class="SelectMenu-title">Notifications</h3>
              <button class="SelectMenu-closeButton" type="button" aria-label="Close menu" data-action="click:notifications-list-subscription-form#closeMenu">
                <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path fill-rule="evenodd" d="M3.72 3.72a.75.75 0 011.06 0L8 6.94l3.22-3.22a.75.75 0 111.06 1.06L9.06 8l3.22 3.22a.75.75 0 11-1.06 1.06L8 9.06l-3.22 3.22a.75.75 0 01-1.06-1.06L6.94 8 3.72 4.78a.75.75 0 010-1.06z"></path>
</svg>
              </button>
            </header>

            <div class="SelectMenu-list">
              <!-- '"` --><!-- </textarea></xmp> --><form data-target="notifications-list-subscription-form.form" data-action="submit:notifications-list-subscription-form#submitForm" data-turbo="false" action="https://github.com/notifications/subscribe" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="2cLEcI5QoDZ1ZfqkVBsQQpf2BcBC7aMlRLZ5WOUelOqbOQARXfWTeQmoZJGZEsodZEs5ir1eAu8UR4cDAulOAg" autocomplete="off">

                <input type="hidden" name="repository_id" value="572068788">

                <button type="submit" name="do" value="included" class="SelectMenu-item flex-items-start" role="menuitemradio" aria-checked="true" data-targets="notifications-list-subscription-form.subscriptionButtons">
                  <span class="f5">
                    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check">
    <path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"></path>
</svg>
                  </span>
                  <div>
                    <div class="f5 text-bold">
                      Participating and @mentions
                    </div>
                    <div class="text-small color-fg-muted text-normal pb-1">
                      Only receive notifications from this repository when participating or @mentioned.
                    </div>
                  </div>
                </button>

                <button type="submit" name="do" value="subscribed" class="SelectMenu-item flex-items-start" role="menuitemradio" aria-checked="false" data-targets="notifications-list-subscription-form.subscriptionButtons">
                  <span class="f5">
                    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check">
    <path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"></path>
</svg>
                  </span>
                  <div>
                    <div class="f5 text-bold">
                      All Activity
                    </div>
                    <div class="text-small color-fg-muted text-normal pb-1">
                      Notified of all notifications on this repository.
                    </div>
                  </div>
                </button>

                <button type="submit" name="do" value="ignore" class="SelectMenu-item flex-items-start" role="menuitemradio" aria-checked="false" data-targets="notifications-list-subscription-form.subscriptionButtons">
                  <span class="f5">
                    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check">
    <path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"></path>
</svg>
                  </span>
                  <div>
                    <div class="f5 text-bold">
                      Ignore
                    </div>
                    <div class="text-small color-fg-muted text-normal pb-1">
                      Never be notified.
                    </div>
                  </div>
                </button>
</form>
              <button class="SelectMenu-item flex-items-start pr-3" type="button" role="menuitemradio" data-target="notifications-list-subscription-form.customButton" data-action="click:notifications-list-subscription-form#openCustomDialog" aria-haspopup="true" aria-checked="false">
                <span class="f5">
                  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check">
    <path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"></path>
</svg>
                </span>
                <div>
                  <div class="d-flex flex-items-start flex-justify-between">
                    <div class="f5 text-bold">Custom</div>
                    <div class="f5 pr-1">
                      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-arrow-right">
    <path fill-rule="evenodd" d="M8.22 2.97a.75.75 0 011.06 0l4.25 4.25a.75.75 0 010 1.06l-4.25 4.25a.75.75 0 01-1.06-1.06l2.97-2.97H3.75a.75.75 0 010-1.5h7.44L8.22 4.03a.75.75 0 010-1.06z"></path>
</svg>
                    </div>
                  </div>
                  <div class="text-small color-fg-muted text-normal pb-1">
                    Select events you want to be notified of in addition to participating and @mentions.
                  </div>
                </div>
              </button>

                <div class="px-3 py-2 d-flex color-bg-subtle flex-items-center">
                  <span class="f5">
                    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-device-mobile SelectMenu-icon SelectMenu-icon--device-mobile">
    <path fill-rule="evenodd" d="M3.75 0A1.75 1.75 0 002 1.75v12.5c0 .966.784 1.75 1.75 1.75h8.5A1.75 1.75 0 0014 14.25V1.75A1.75 1.75 0 0012.25 0h-8.5zM3.5 1.75a.25.25 0 01.25-.25h8.5a.25.25 0 01.25.25v12.5a.25.25 0 01-.25.25h-8.5a.25.25 0 01-.25-.25V1.75zM8 13a1 1 0 100-2 1 1 0 000 2z"></path>
</svg>
                  </span>
                  <span classname="text-small color-fg-muted text-normal pb-1">
                    Get push notifications on <a target="_blank" rel="noopener noreferrer" href="https://apps.apple.com/app/apple-store/id1477376905?ct=watch-dropdown&amp;mt=8&amp;pt=524675">iOS</a> or <a target="_blank" rel="noopener noreferrer" href="https://play.google.com/store/apps/details?id=com.github.android&amp;referrer=utm_campaign%3Dwatch-dropdown%26utm_medium%3Dweb%26utm_source%3Dgithub">Android</a>.
                  </span>
                </div>
            </div>
          </div>
        <span class="sentinel" tabindex="0" aria-hidden="true"></span></details-menu>

        <details-dialog class="notifications-component-dialog " data-target="notifications-list-subscription-form.customDialog" aria-label="Custom dialog" hidden="" role="dialog" aria-modal="true">
          <div class="SelectMenu-modal notifications-component-dialog-modal overflow-visible">
            <!-- '"` --><!-- </textarea></xmp> --><form data-target="notifications-list-subscription-form.customform" data-action="submit:notifications-list-subscription-form#submitCustomForm" data-turbo="false" action="https://github.com/notifications/subscribe" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="ptMw6YevfLioz3_mVc7FRV6gYNXngWk_po5B6uJ4WqTkKPSIVApP99QC4dOYxx8arR1cnxgyyPX2f7-xBY-ATA" autocomplete="off">

              <input type="hidden" name="repository_id" value="572068788">

              <header class="d-sm-none SelectMenu-header pb-0 border-bottom-0 px-2 px-sm-3">
                <h1 class="f3 SelectMenu-title d-inline-flex">
                  <button class="color-bg-default border-0 px-2 py-0 m-0 Link--secondary f5" aria-label="Return to menu" type="button" data-action="click:notifications-list-subscription-form#closeCustomDialog">
                    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-arrow-left">
    <path fill-rule="evenodd" d="M7.78 12.53a.75.75 0 01-1.06 0L2.47 8.28a.75.75 0 010-1.06l4.25-4.25a.75.75 0 011.06 1.06L4.81 7h7.44a.75.75 0 010 1.5H4.81l2.97 2.97a.75.75 0 010 1.06z"></path>
</svg>
                  </button>
                  Custom
                </h1>
              </header>

              <header class="d-none d-sm-flex flex-items-start pt-1">
                <button class="border-0 px-2 pt-1 m-0 Link--secondary f5" style="background-color: transparent;" aria-label="Return to menu" type="button" data-action="click:notifications-list-subscription-form#closeCustomDialog">
                  <svg style="position: relative; left: 2px; top: 1px" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-arrow-left">
    <path fill-rule="evenodd" d="M7.78 12.53a.75.75 0 01-1.06 0L2.47 8.28a.75.75 0 010-1.06l4.25-4.25a.75.75 0 011.06 1.06L4.81 7h7.44a.75.75 0 010 1.5H4.81l2.97 2.97a.75.75 0 010 1.06z"></path>
</svg>
                </button>

                <h1 class="pt-1 pr-4 pb-0 pl-0 f5 text-bold">
                  Custom
                </h1>
              </header>

              <fieldset>
                <legend>
                  <div class="text-small color-fg-muted pt-0 pr-3 pb-3 pl-6 pl-sm-5 border-bottom mb-3">
                    Select events you want to be notified of in addition to participating and @mentions.
                  </div>
                </legend>
                <div data-target="notifications-list-subscription-form.labelInputs">
                </div>
                  <div class="form-checkbox mr-3 ml-6 ml-sm-5 mb-2 mt-0">
                    <label class="f5 text-normal">
                      <input type="checkbox" name="thread_types[]" value="Issue" data-targets="notifications-list-subscription-form.threadTypeCheckboxes" data-action="change:notifications-list-subscription-form#threadTypeCheckboxesUpdated">
                      Issues
                    </label>


                  </div>
                  <div class="form-checkbox mr-3 ml-6 ml-sm-5 mb-2 mt-0">
                    <label class="f5 text-normal">
                      <input type="checkbox" name="thread_types[]" value="PullRequest" data-targets="notifications-list-subscription-form.threadTypeCheckboxes" data-action="change:notifications-list-subscription-form#threadTypeCheckboxesUpdated">
                      Pull requests
                    </label>


                  </div>
                  <div class="form-checkbox mr-3 ml-6 ml-sm-5 mb-2 mt-0">
                    <label class="f5 text-normal">
                      <input type="checkbox" name="thread_types[]" value="Release" data-targets="notifications-list-subscription-form.threadTypeCheckboxes" data-action="change:notifications-list-subscription-form#threadTypeCheckboxesUpdated">
                      Releases
                    </label>


                  </div>
                  <div class="form-checkbox mr-3 ml-6 ml-sm-5 mb-2 mt-0">
                    <label class="f5 text-normal">
                      <input type="checkbox" name="thread_types[]" value="Discussion" data-targets="notifications-list-subscription-form.threadTypeCheckboxes" data-action="change:notifications-list-subscription-form#threadTypeCheckboxesUpdated" aria-describedby="Discussion-disabled" aria-disabled="true">
                      Discussions
                    </label>

                      <div id="Discussion-disabled" class="color-fg-muted">
                        Discussions are not enabled for this repository
                      </div>

                  </div>
                  <div class="form-checkbox mr-3 ml-6 ml-sm-5 mb-2 mt-0">
                    <label class="f5 text-normal">
                      <input type="checkbox" name="thread_types[]" value="SecurityAlert" data-targets="notifications-list-subscription-form.threadTypeCheckboxes" data-action="change:notifications-list-subscription-form#threadTypeCheckboxesUpdated">
                      Security alerts
                    </label>


                  </div>
              </fieldset>
              <div class="pt-2 pb-3 px-3 d-flex flex-justify-start flex-row-reverse">
                  <button name="do" value="custom" data-target="notifications-list-subscription-form.customSubmit" disabled="disabled" type="submit" data-view-component="true" class="btn-primary btn-sm btn ml-2">    Apply
</button>

                  <button data-action="click:notifications-list-subscription-form#resetForm" data-close-dialog="" type="button" data-view-component="true" class="btn-sm btn">    Cancel
</button>
              </div>
</form>          </div>
        </details-dialog>


        <div class="notifications-component-dialog-overlay"></div>
      </details>
    </notifications-list-subscription-form>



  </li>

  <li>
        <div data-view-component="true" class="d-flex">
        <div data-view-component="true" class="position-relative d-inline-block">
    <a icon="repo-forked" id="fork-button" href="https://github.com/reyashv/python/fork" data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;FORK_BUTTON&quot;,&quot;repository_id&quot;:572068788,&quot;originating_url&quot;:&quot;https://github.com/reyashv/python&quot;,&quot;user_id&quot;:124596951}}" data-hydro-click-hmac="b497b6be857884c46a299a553971e8f0226cb16b2e9fc05b549445201874cb0a" data-ga-click="Repository, show fork modal, action:files#disambiguate; text:Fork" data-view-component="true" class="btn-sm btn BtnGroup-item border-right-0" aria-describedby="tooltip-d8410716-12a9-4e5f-b1ec-6c6ebb62beb2">      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo-forked mr-2">
    <path fill-rule="evenodd" d="M5 3.25a.75.75 0 11-1.5 0 .75.75 0 011.5 0zm0 2.122a2.25 2.25 0 10-1.5 0v.878A2.25 2.25 0 005.75 8.5h1.5v2.128a2.251 2.251 0 101.5 0V8.5h1.5a2.25 2.25 0 002.25-2.25v-.878a2.25 2.25 0 10-1.5 0v.878a.75.75 0 01-.75.75h-4.5A.75.75 0 015 6.25v-.878zm3.75 7.378a.75.75 0 11-1.5 0 .75.75 0 011.5 0zm3-8.75a.75.75 0 100-1.5.75.75 0 000 1.5z"></path>
</svg>Fork
          <span id="repo-network-counter" data-pjax-replace="true" data-turbo-replace="true" title="0" data-view-component="true" class="Counter">0</span>
</a>    <tool-tip id="tooltip-d8410716-12a9-4e5f-b1ec-6c6ebb62beb2" for="fork-button" data-direction="s" data-type="description" data-view-component="true" class="sr-only position-absolute" role="tooltip">Fork your own copy of reyashv/python</tool-tip>
</div>
      <details group_item="true" id="my-forks-menu-572068788" data-view-component="true" class="details-reset details-overlay BtnGroup-parent d-inline-block position-relative">
              <summary aria-label="See your forks of this repository" data-view-component="true" class="btn-sm btn BtnGroup-item px-2 float-none" aria-haspopup="menu" role="button">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-triangle-down">
    <path d="M4.427 7.427l3.396 3.396a.25.25 0 00.354 0l3.396-3.396A.25.25 0 0011.396 7H4.604a.25.25 0 00-.177.427z"></path>
</svg>
</summary>
  <details-menu class="SelectMenu right-0" src="/reyashv/python/my_forks_menu_content?can_fork=true" role="menu" data-focus-trap="suspended"><span class="sentinel" tabindex="0" aria-hidden="true"></span>
    <div class="SelectMenu-modal">
        <button class="SelectMenu-closeButton position-absolute right-0 m-2" type="button" aria-label="Close menu" data-toggle-for="details-3d4414">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path fill-rule="evenodd" d="M3.72 3.72a.75.75 0 011.06 0L8 6.94l3.22-3.22a.75.75 0 111.06 1.06L9.06 8l3.22 3.22a.75.75 0 11-1.06 1.06L8 9.06l-3.22 3.22a.75.75 0 01-1.06-1.06L6.94 8 3.72 4.78a.75.75 0 010-1.06z"></path>
</svg>
        </button>
      <div id="filter-menu-3d4414" class="d-flex flex-column flex-1 overflow-hidden">
        <div class="SelectMenu-list">

            <include-fragment class="SelectMenu-loading" aria-label="Loading">
              <svg role="menuitem" style="box-sizing: content-box; color: var(--color-icon-primary);" width="32" height="32" viewBox="0 0 16 16" fill="none" data-view-component="true" class="anim-rotate">
  <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke"></circle>
  <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke"></path>
</svg>
            </include-fragment>
        </div>
        
      </div>
    </div>
  <span class="sentinel" tabindex="0" aria-hidden="true"></span></details-menu>
</details></div>
  </li>

  <li>
        <template class="js-unstar-confirmation-dialog-template"></template>

  <div data-view-component="true" class="js-toggler-container js-social-container starring-container d-flex">
    <div data-view-component="true" class="starred BtnGroup flex-1">
      <!-- '"` --><!-- </textarea></xmp> --><form class="js-social-form BtnGroup-parent flex-auto js-deferred-toggler-target" data-turbo="false" action="https://github.com/reyashv/python/unstar" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="-iWwJACbc81b6AQjkehnun93OO0isGItUXtkQX_kSxyFlI9_G2i6rE_jAttsnHN7duz6M7TUAOmP2eLW0YZkGA" autocomplete="off">
          <input type="hidden" value="dfvNy4Cg8CVcd5C_KMrrpP_pwcOVtQ0lrWIV2tsqHU0KSvKQm1M5REh8lkfVvv9l9nIDHQPRb-FzwJNNdUgySQ" data-csrf="true" class="js-confirm-csrf-token">
        <input type="hidden" name="context" value="repository">
          <button data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;UNSTAR_BUTTON&quot;,&quot;repository_id&quot;:572068788,&quot;originating_url&quot;:&quot;https://github.com/reyashv/python&quot;,&quot;user_id&quot;:124596951}}" data-hydro-click-hmac="a21cea543732a5853adb96fe3681ada5918e117208e9f2817da304a4dcff66c3" data-ga-click="Repository, click unstar button, action:files#disambiguate; text:Unstar" aria-label="Unstar this repository (0)" type="submit" data-view-component="true" class="rounded-left-2 btn-sm btn BtnGroup-item">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-star-fill starred-button-icon d-inline-block mr-2">
    <path fill-rule="evenodd" d="M8 .25a.75.75 0 01.673.418l1.882 3.815 4.21.612a.75.75 0 01.416 1.279l-3.046 2.97.719 4.192a.75.75 0 01-1.088.791L8 12.347l-3.766 1.98a.75.75 0 01-1.088-.79l.72-4.194L.818 6.374a.75.75 0 01.416-1.28l4.21-.611L7.327.668A.75.75 0 018 .25z"></path>
</svg><span data-view-component="true" class="d-inline">
            Starred
</span>            <span id="repo-stars-counter-unstar" aria-label="0 users starred this repository" data-singular-suffix="user starred this repository" data-plural-suffix="users starred this repository" data-turbo-replace="true" title="0" data-view-component="true" class="Counter js-social-count">0</span>
</button></form>        <details id="details-user-list-572068788" data-view-component="true" class="details-reset details-overlay BtnGroup-parent js-user-list-menu d-inline-block position-relative">
        <summary aria-label="Add this repository to a list" data-view-component="true" class="btn-sm btn BtnGroup-item px-2 float-none" aria-haspopup="menu" role="button">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-triangle-down">
    <path d="M4.427 7.427l3.396 3.396a.25.25 0 00.354 0l3.396-3.396A.25.25 0 0011.396 7H4.604a.25.25 0 00-.177.427z"></path>
</svg>
</summary>
  <details-menu class="SelectMenu right-0" src="/reyashv/python/lists" role="menu" data-focus-trap="suspended"><span class="sentinel" tabindex="0" aria-hidden="true"></span>
    <div class="SelectMenu-modal">
        <button class="SelectMenu-closeButton position-absolute right-0 m-2" type="button" aria-label="Close menu" data-toggle-for="details-916b16">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path fill-rule="evenodd" d="M3.72 3.72a.75.75 0 011.06 0L8 6.94l3.22-3.22a.75.75 0 111.06 1.06L9.06 8l3.22 3.22a.75.75 0 11-1.06 1.06L8 9.06l-3.22 3.22a.75.75 0 01-1.06-1.06L6.94 8 3.72 4.78a.75.75 0 010-1.06z"></path>
</svg>
        </button>
      <div id="filter-menu-916b16" class="d-flex flex-column flex-1 overflow-hidden">
        <div class="SelectMenu-list">

            <include-fragment class="SelectMenu-loading" aria-label="Loading">
              <svg role="menuitem" style="box-sizing: content-box; color: var(--color-icon-primary);" width="32" height="32" viewBox="0 0 16 16" fill="none" data-view-component="true" class="anim-rotate">
  <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke"></circle>
  <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke"></path>
</svg>
            </include-fragment>
        </div>
        
      </div>
    </div>
  <span class="sentinel" tabindex="0" aria-hidden="true"></span></details-menu>
</details>
</div>
    <div data-view-component="true" class="unstarred BtnGroup flex-1">
      <!-- '"` --><!-- </textarea></xmp> --><form class="js-social-form BtnGroup-parent flex-auto" data-turbo="false" action="https://github.com/reyashv/python/star" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="bbLSz3q6hr4xgCxVTLLO872OgVtPYk5QRl2CeUuxW6SEDURq6soQgnO6vjdsTM5MF5adcquY4apRlx6vH6f6Hw" autocomplete="off">
        <input type="hidden" name="context" value="repository">
          <button data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;STAR_BUTTON&quot;,&quot;repository_id&quot;:572068788,&quot;originating_url&quot;:&quot;https://github.com/reyashv/python&quot;,&quot;user_id&quot;:124596951}}" data-hydro-click-hmac="3c9d17ad7922d4d42dc775350e4e2c4b819d9ed8defb6e2675da34ecd5b1bb39" data-ga-click="Repository, click star button, action:files#disambiguate; text:Star" aria-label="Star this repository (0)" type="submit" data-view-component="true" class="js-toggler-target rounded-left-2 btn-sm btn BtnGroup-item">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-star d-inline-block mr-2">
    <path fill-rule="evenodd" d="M8 .25a.75.75 0 01.673.418l1.882 3.815 4.21.612a.75.75 0 01.416 1.279l-3.046 2.97.719 4.192a.75.75 0 01-1.088.791L8 12.347l-3.766 1.98a.75.75 0 01-1.088-.79l.72-4.194L.818 6.374a.75.75 0 01.416-1.28l4.21-.611L7.327.668A.75.75 0 018 .25zm0 2.445L6.615 5.5a.75.75 0 01-.564.41l-3.097.45 2.24 2.184a.75.75 0 01.216.664l-.528 3.084 2.769-1.456a.75.75 0 01.698 0l2.77 1.456-.53-3.084a.75.75 0 01.216-.664l2.24-2.183-3.096-.45a.75.75 0 01-.564-.41L8 2.694v.001z"></path>
</svg><span data-view-component="true" class="d-inline">
            Star
</span>            <span id="repo-stars-counter-star" aria-label="0 users starred this repository" data-singular-suffix="user starred this repository" data-plural-suffix="users starred this repository" data-turbo-replace="true" title="0" data-view-component="true" class="Counter js-social-count">0</span>
</button></form>        <details id="details-user-list-572068788" data-view-component="true" class="details-reset details-overlay BtnGroup-parent js-user-list-menu d-inline-block position-relative">
        <summary aria-label="Add this repository to a list" data-view-component="true" class="btn-sm btn BtnGroup-item px-2 float-none" aria-haspopup="menu" role="button">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-triangle-down">
    <path d="M4.427 7.427l3.396 3.396a.25.25 0 00.354 0l3.396-3.396A.25.25 0 0011.396 7H4.604a.25.25 0 00-.177.427z"></path>
</svg>
</summary>
  <details-menu class="SelectMenu right-0" src="/reyashv/python/lists" role="menu" data-focus-trap="suspended"><span class="sentinel" tabindex="0" aria-hidden="true"></span>
    <div class="SelectMenu-modal">
        <button class="SelectMenu-closeButton position-absolute right-0 m-2" type="button" aria-label="Close menu" data-toggle-for="details-916b16">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path fill-rule="evenodd" d="M3.72 3.72a.75.75 0 011.06 0L8 6.94l3.22-3.22a.75.75 0 111.06 1.06L9.06 8l3.22 3.22a.75.75 0 11-1.06 1.06L8 9.06l-3.22 3.22a.75.75 0 01-1.06-1.06L6.94 8 3.72 4.78a.75.75 0 010-1.06z"></path>
</svg>
        </button>
      <div id="filter-menu-916b16" class="d-flex flex-column flex-1 overflow-hidden">
        <div class="SelectMenu-list">

            <include-fragment class="SelectMenu-loading" aria-label="Loading">
              <svg role="menuitem" style="box-sizing: content-box; color: var(--color-icon-primary);" width="32" height="32" viewBox="0 0 16 16" fill="none" data-view-component="true" class="anim-rotate">
  <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke"></circle>
  <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke"></path>
</svg>
            </include-fragment>
        </div>
        
      </div>
    </div>
  <span class="sentinel" tabindex="0" aria-hidden="true"></span></details-menu>
</details>
</div></div>
  </li>

    

</ul>

      </div>

        <div id="responsive-meta-container" data-turbo-replace="">
</div>


          <nav data-pjax="#js-repo-pjax-container" aria-label="Repository" data-view-component="true" class="js-repo-nav js-sidenav-container-pjax js-responsive-underlinenav overflow-hidden UnderlineNav px-3 px-md-4 px-lg-5">

  <ul data-view-component="true" class="UnderlineNav-body list-style-none">
      <li data-view-component="true" class="d-inline-flex">
  <a id="code-tab" href="https://github.com/reyashv/python" data-tab-item="i0code-tab" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages repo_deployments /reyashv/python" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g c" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Code&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" aria-current="page" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item selected">
    
                <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-code UnderlineNav-octicon d-none d-sm-inline">
    <path fill-rule="evenodd" d="M4.72 3.22a.75.75 0 011.06 1.06L2.06 8l3.72 3.72a.75.75 0 11-1.06 1.06L.47 8.53a.75.75 0 010-1.06l4.25-4.25zm6.56 0a.75.75 0 10-1.06 1.06L13.94 8l-3.72 3.72a.75.75 0 101.06 1.06l4.25-4.25a.75.75 0 000-1.06l-4.25-4.25z"></path>
</svg>
        <span data-content="Code">Code</span>
          <span id="code-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="issues-tab" href="https://github.com/reyashv/python/issues" data-tab-item="i1issues-tab" data-selected-links="repo_issues repo_labels repo_milestones /reyashv/python/issues" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g i" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Issues&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
                <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-issue-opened UnderlineNav-octicon d-none d-sm-inline">
    <path d="M8 9.5a1.5 1.5 0 100-3 1.5 1.5 0 000 3z"></path><path fill-rule="evenodd" d="M8 0a8 8 0 100 16A8 8 0 008 0zM1.5 8a6.5 6.5 0 1113 0 6.5 6.5 0 01-13 0z"></path>
</svg>
        <span data-content="Issues">Issues</span>
          <span id="issues-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="0" hidden="hidden" data-view-component="true" class="Counter">0</span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="pull-requests-tab" href="https://github.com/reyashv/python/pulls" data-tab-item="i2pull-requests-tab" data-selected-links="repo_pulls checks /reyashv/python/pulls" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g p" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Pull requests&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
                <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-pull-request UnderlineNav-octicon d-none d-sm-inline">
    <path fill-rule="evenodd" d="M7.177 3.073L9.573.677A.25.25 0 0110 .854v4.792a.25.25 0 01-.427.177L7.177 3.427a.25.25 0 010-.354zM3.75 2.5a.75.75 0 100 1.5.75.75 0 000-1.5zm-2.25.75a2.25 2.25 0 113 2.122v5.256a2.251 2.251 0 11-1.5 0V5.372A2.25 2.25 0 011.5 3.25zM11 2.5h-1V4h1a1 1 0 011 1v5.628a2.251 2.251 0 101.5 0V5A2.5 2.5 0 0011 2.5zm1 10.25a.75.75 0 111.5 0 .75.75 0 01-1.5 0zM3.75 12a.75.75 0 100 1.5.75.75 0 000-1.5z"></path>
</svg>
        <span data-content="Pull requests">Pull requests</span>
          <span id="pull-requests-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="0" hidden="hidden" data-view-component="true" class="Counter">0</span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="actions-tab" href="https://github.com/reyashv/python/actions" data-tab-item="i3actions-tab" data-selected-links="repo_actions /reyashv/python/actions" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g a" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Actions&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
                <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-play UnderlineNav-octicon d-none d-sm-inline">
    <path fill-rule="evenodd" d="M1.5 8a6.5 6.5 0 1113 0 6.5 6.5 0 01-13 0zM8 0a8 8 0 100 16A8 8 0 008 0zM6.379 5.227A.25.25 0 006 5.442v5.117a.25.25 0 00.379.214l4.264-2.559a.25.25 0 000-.428L6.379 5.227z"></path>
</svg>
        <span data-content="Actions">Actions</span>
          <span id="actions-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="projects-tab" href="https://github.com/reyashv/python/projects" data-tab-item="i4projects-tab" data-selected-links="repo_projects new_repo_project repo_project /reyashv/python/projects" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g b" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Projects&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
                <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-table UnderlineNav-octicon d-none d-sm-inline">
    <path fill-rule="evenodd" d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0114.25 16H1.75A1.75 1.75 0 010 14.25V1.75zM1.5 6.5v7.75c0 .138.112.25.25.25H5v-8H1.5zM5 5H1.5V1.75a.25.25 0 01.25-.25H5V5zm1.5 1.5v8h7.75a.25.25 0 00.25-.25V6.5h-8zm8-1.5h-8V1.5h7.75a.25.25 0 01.25.25V5z"></path>
</svg>
        <span data-content="Projects">Projects</span>
          <span id="projects-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="0" hidden="hidden" data-view-component="true" class="Counter">0</span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="security-tab" href="https://github.com/reyashv/python/security" data-tab-item="i5security-tab" data-selected-links="security overview alerts policy token_scanning code_scanning /reyashv/python/security" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g s" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Security&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
                <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-shield UnderlineNav-octicon d-none d-sm-inline">
    <path fill-rule="evenodd" d="M7.467.133a1.75 1.75 0 011.066 0l5.25 1.68A1.75 1.75 0 0115 3.48V7c0 1.566-.32 3.182-1.303 4.682-.983 1.498-2.585 2.813-5.032 3.855a1.7 1.7 0 01-1.33 0c-2.447-1.042-4.049-2.357-5.032-3.855C1.32 10.182 1 8.566 1 7V3.48a1.75 1.75 0 011.217-1.667l5.25-1.68zm.61 1.429a.25.25 0 00-.153 0l-5.25 1.68a.25.25 0 00-.174.238V7c0 1.358.275 2.666 1.057 3.86.784 1.194 2.121 2.34 4.366 3.297a.2.2 0 00.154 0c2.245-.956 3.582-2.104 4.366-3.298C13.225 9.666 13.5 8.36 13.5 7V3.48a.25.25 0 00-.174-.237l-5.25-1.68zM9 10.5a1 1 0 11-2 0 1 1 0 012 0zm-.25-5.75a.75.75 0 10-1.5 0v3a.75.75 0 001.5 0v-3z"></path>
</svg>
        <span data-content="Security">Security</span>
          

    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="insights-tab" href="https://github.com/reyashv/python/network/dependencies" data-tab-item="i6insights-tab" data-selected-links="repo_graphs repo_contributors dependency_graph dependabot_updates pulse people community /reyashv/python/network/dependencies" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Insights&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
                <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-graph UnderlineNav-octicon d-none d-sm-inline">
    <path fill-rule="evenodd" d="M1.5 1.75a.75.75 0 00-1.5 0v12.5c0 .414.336.75.75.75h14.5a.75.75 0 000-1.5H1.5V1.75zm14.28 2.53a.75.75 0 00-1.06-1.06L10 7.94 7.53 5.47a.75.75 0 00-1.06 0L3.22 8.72a.75.75 0 001.06 1.06L7 7.06l2.47 2.47a.75.75 0 001.06 0l5.25-5.25z"></path>
</svg>
        <span data-content="Insights">Insights</span>
          <span id="insights-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
</ul>
    <div style="visibility:hidden;" data-view-component="true" class="UnderlineNav-actions js-responsive-underlinenav-overflow position-absolute pr-3 pr-md-4 pr-lg-5 right-0">      <details data-view-component="true" class="details-overlay details-reset position-relative">
  <summary role="button" data-view-component="true" aria-haspopup="menu">          <div class="UnderlineNav-item mr-0 border-0">
            <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-kebab-horizontal">
    <path d="M8 9a1.5 1.5 0 100-3 1.5 1.5 0 000 3zM1.5 9a1.5 1.5 0 100-3 1.5 1.5 0 000 3zm13 0a1.5 1.5 0 100-3 1.5 1.5 0 000 3z"></path>
</svg>
            <span class="sr-only">More</span>
          </div>
</summary>
  <details-menu role="menu" data-view-component="true" class="dropdown-menu dropdown-menu-sw" data-focus-trap="suspended"><span class="sentinel" tabindex="0" aria-hidden="true"></span>          <ul>
              <li data-menu-item="i0code-tab" hidden="">
                <a role="menuitem" class="js-selected-navigation-item selected dropdown-item" aria-current="page" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages repo_deployments /reyashv/python" href="https://github.com/reyashv/python">
                  Code
</a>              </li>
              <li data-menu-item="i1issues-tab" hidden="">
                <a role="menuitem" class="js-selected-navigation-item dropdown-item" data-selected-links="repo_issues repo_labels repo_milestones /reyashv/python/issues" href="https://github.com/reyashv/python/issues">
                  Issues
</a>              </li>
              <li data-menu-item="i2pull-requests-tab" hidden="">
                <a role="menuitem" class="js-selected-navigation-item dropdown-item" data-selected-links="repo_pulls checks /reyashv/python/pulls" href="https://github.com/reyashv/python/pulls">
                  Pull requests
</a>              </li>
              <li data-menu-item="i3actions-tab" hidden="">
                <a role="menuitem" class="js-selected-navigation-item dropdown-item" data-selected-links="repo_actions /reyashv/python/actions" href="https://github.com/reyashv/python/actions">
                  Actions
</a>              </li>
              <li data-menu-item="i4projects-tab" hidden="">
                <a role="menuitem" class="js-selected-navigation-item dropdown-item" data-selected-links="repo_projects new_repo_project repo_project /reyashv/python/projects" href="https://github.com/reyashv/python/projects">
                  Projects
</a>              </li>
              <li data-menu-item="i5security-tab" hidden="">
                <a role="menuitem" class="js-selected-navigation-item dropdown-item" data-selected-links="security overview alerts policy token_scanning code_scanning /reyashv/python/security" href="https://github.com/reyashv/python/security">
                  Security
</a>              </li>
              <li data-menu-item="i6insights-tab" hidden="">
                <a role="menuitem" class="js-selected-navigation-item dropdown-item" data-selected-links="repo_graphs repo_contributors dependency_graph dependabot_updates pulse people community /reyashv/python/network/dependencies" href="https://github.com/reyashv/python/network/dependencies">
                  Insights
</a>              </li>
          </ul>
<span class="sentinel" tabindex="0" aria-hidden="true"></span></details-menu>
</details></div>
</nav>

  </div>

  



  <turbo-frame id="repo-content-turbo-frame" target="_top" data-turbo-action="advance" class="" src="https://github.com/reyashv/python/blob/main/tkinterproject.py" complete="">
      <a href="https://github.dev/" class="d-none js-github-dev-shortcut" data-hotkey=".">Open in github.dev</a>
  <a href="https://github.dev/" class="d-none js-github-dev-new-tab-shortcut" data-hotkey="Shift+.,Shift+&gt;,&gt;" target="_blank">Open in a new github.dev tab</a>

    
  <div class="clearfix container-xl px-3 px-md-4 px-lg-5 mt-4">
    <div class="mb-3">
  <span data-view-component="true" class="Label Label--success">Beta</span>
  <a class="text-small" href="https://github.com/reyashv/python/blob/main/tkinterproject.py#enroll-beta" data-feature-preview-trigger-url="/users/samyuktaakannan/feature_previews?selected_slug=code_search_code_view">
     Try the new code view
  </a>
</div>

    
    
<div>
  

  



    
<a class="d-none js-permalink-shortcut" data-hotkey="y" href="https://github.com/reyashv/python/blob/6896039a3a2afc5582fe93390554dd72d0023ef8/tkinterproject.py">Permalink</a>

<div class="d-flex flex-items-start flex-shrink-0 pb-3 flex-wrap flex-md-nowrap flex-justify-between flex-md-justify-start">
  
<div class="position-relative">
  <details class="js-branch-select-menu details-reset details-overlay mr-0 mb-0 " id="branch-select-menu" data-hydro-click-payload="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;REFS_SELECTOR_MENU&quot;,&quot;repository_id&quot;:572068788,&quot;originating_url&quot;:&quot;https://github.com/reyashv/python/blob/main/tkinterproject.py&quot;,&quot;user_id&quot;:124596951}}" data-hydro-click-hmac="fcbbaf63e4b22d0e63e33ac27471726634faf23409908750764f6de579f65520">
    <summary class="btn css-truncate" data-hotkey="w" title="Switch branches or tags">
      <svg text="gray" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-branch">
    <path fill-rule="evenodd" d="M11.75 2.5a.75.75 0 100 1.5.75.75 0 000-1.5zm-2.25.75a2.25 2.25 0 113 2.122V6A2.5 2.5 0 0110 8.5H6a1 1 0 00-1 1v1.128a2.251 2.251 0 11-1.5 0V5.372a2.25 2.25 0 111.5 0v1.836A2.492 2.492 0 016 7h4a1 1 0 001-1v-.628A2.25 2.25 0 019.5 3.25zM4.25 12a.75.75 0 100 1.5.75.75 0 000-1.5zM3.5 3.25a.75.75 0 111.5 0 .75.75 0 01-1.5 0z"></path>
</svg>
      <span class="css-truncate-target" data-menu-button="">main</span>
      <span class="dropdown-caret"></span>
    </summary>

    
<div class="SelectMenu">
  <div class="SelectMenu-modal">
    <header class="SelectMenu-header">
      <span class="SelectMenu-title">Switch branches/tags</span>
      <button class="SelectMenu-closeButton" type="button" data-toggle-for="branch-select-menu"><svg aria-label="Close menu" aria-hidden="false" role="img" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path fill-rule="evenodd" d="M3.72 3.72a.75.75 0 011.06 0L8 6.94l3.22-3.22a.75.75 0 111.06 1.06L9.06 8l3.22 3.22a.75.75 0 11-1.06 1.06L8 9.06l-3.22 3.22a.75.75 0 01-1.06-1.06L6.94 8 3.72 4.78a.75.75 0 010-1.06z"></path>
</svg></button>
    </header>

    <input-demux data-action="tab-container-change:input-demux#storeInput tab-container-changed:input-demux#updateInput" data-catalyst="">
      <tab-container class="d-flex flex-column js-branches-tags-tabs" style="min-height: 0;">
        <div class="SelectMenu-filter">
          <input data-target="input-demux.source" id="context-commitish-filter-field" class="SelectMenu-input form-control" aria-owns="ref-list-branches" data-controls-ref-menu-id="ref-list-branches" autofocus="" autocomplete="off" aria-label="Find or create a branch…" placeholder="Find or create a branch…" type="text">
        </div>

        <div class="SelectMenu-tabs" role="tablist" data-target="input-demux.control">
          <button class="SelectMenu-tab" type="button" role="tab" aria-selected="true" tabindex="0">Branches</button>
          <button class="SelectMenu-tab" type="button" role="tab" aria-selected="false" tabindex="-1">Tags</button>
        </div>

        <div role="tabpanel" id="ref-list-branches" data-filter-placeholder="Find or create a branch…" tabindex="" class="d-flex flex-column flex-auto overflow-auto">
          <ref-selector type="branch" data-targets="input-demux.sinks" data-action="
              input-entered:ref-selector#inputEntered
              tab-selected:ref-selector#tabSelected
              focus-list:ref-selector#focusFirstListMember
            " query-endpoint="/reyashv/python/refs" can-create="" cache-key="v0:1669729716.59326" current-committish="bWFpbg==" default-branch="bWFpbg==" name-with-owner="cmV5YXNodi9weXRob24=" prefetch-on-mouseover="" data-catalyst="">

            <template data-target="ref-selector.fetchFailedTemplate"></template>

              <template data-target="ref-selector.noMatchTemplate"></template>


            <div data-target="ref-selector.listContainer" role="menu" class="SelectMenu-list " data-turbo-frame="repo-content-turbo-frame">
              <div class="SelectMenu-loading pt-3 pb-0 overflow-hidden" aria-label="Menu is loading">
                <svg style="box-sizing: content-box; color: var(--color-icon-primary);" width="32" height="32" viewBox="0 0 16 16" fill="none" data-view-component="true" class="anim-rotate">
  <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke"></circle>
  <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke"></path>
</svg>
              </div>
            </div>

              

<template data-target="ref-selector.itemTemplate"></template>


              <footer class="SelectMenu-footer"><a href="https://github.com/reyashv/python/branches">View all branches</a></footer>
          </ref-selector>

        </div>

        <div role="tabpanel" id="tags-menu" data-filter-placeholder="Find a tag" tabindex="" hidden="" class="d-flex flex-column flex-auto overflow-auto">
          <ref-selector type="tag" data-action="
              input-entered:ref-selector#inputEntered
              tab-selected:ref-selector#tabSelected
              focus-list:ref-selector#focusFirstListMember
            " data-targets="input-demux.sinks" query-endpoint="/reyashv/python/refs" cache-key="v0:1669729716.59326" current-committish="bWFpbg==" default-branch="bWFpbg==" name-with-owner="cmV5YXNodi9weXRob24=" data-catalyst="">

            <template data-target="ref-selector.fetchFailedTemplate"></template>

            <template data-target="ref-selector.noMatchTemplate"></template>

              

<template data-target="ref-selector.itemTemplate"></template>


            <div data-target="ref-selector.listContainer" role="menu" class="SelectMenu-list" data-turbo-frame="repo-content-turbo-frame">
              <div class="SelectMenu-loading pt-3 pb-0 overflow-hidden" aria-label="Menu is loading">
                <svg style="box-sizing: content-box; color: var(--color-icon-primary);" width="32" height="32" viewBox="0 0 16 16" fill="none" data-view-component="true" class="anim-rotate">
  <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke"></circle>
  <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke"></path>
</svg>
              </div>
            </div>
              <footer class="SelectMenu-footer"><a href="https://github.com/reyashv/python/tags">View all tags</a></footer>
          </ref-selector>
        </div>
      </tab-container>
    </input-demux>
  </div>
</div>

  </details>

</div>


<div class="Overlay--hidden Overlay-backdrop--center" data-modal-dialog-overlay="">
  <modal-dialog role="dialog" id="warn-tag-match-create-branch-dialog" aria-modal="true" aria-labelledby="warn-tag-match-create-branch-dialog-header" data-view-component="true" class="Overlay Overlay--width-large Overlay--height-auto Overlay--motion-scaleFade">
      <header class="Overlay-header Overlay-header--large Overlay-header--divided">
        <div class="Overlay-headerContentWrap">
          <div class="Overlay-titleWrap">
            <h1 id="warn-tag-match-create-branch-dialog-header" class="Overlay-title">Name already in use</h1>
          </div>
          <div class="Overlay-actionWrap">
            <button data-close-dialog-id="warn-tag-match-create-branch-dialog" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path fill-rule="evenodd" d="M3.72 3.72a.75.75 0 011.06 0L8 6.94l3.22-3.22a.75.75 0 111.06 1.06L9.06 8l3.22 3.22a.75.75 0 11-1.06 1.06L8 9.06l-3.22 3.22a.75.75 0 01-1.06-1.06L6.94 8 3.72 4.78a.75.75 0 010-1.06z"></path>
</svg></button>
          </div>
        </div>
      </header>
    <div class="Overlay-body ">
      
          <div data-view-component="true">      A tag already exists with the provided branch name. Many Git commands accept both tag and branch names, so creating this branch may cause unexpected behavior. Are you sure you want to create this branch?
</div>

    </div>
      <footer class="Overlay-footer Overlay-footer--alignEnd">
            <button data-close-dialog-id="warn-tag-match-create-branch-dialog" type="button" data-view-component="true" class="btn">    Cancel
</button>
            <button data-submit-dialog-id="warn-tag-match-create-branch-dialog" type="button" data-view-component="true" class="btn-danger btn">    Create
</button>
      </footer>
</modal-dialog></div>


  <h2 id="blob-path" class="breadcrumb flex-auto flex-self-center min-width-0 text-normal mx-2 width-full width-md-auto flex-order-1 flex-md-order-none mt-3 mt-md-0">
    <span class="js-repo-root text-bold"><span class="js-path-segment d-inline-block wb-break-all"><a data-turbo-frame="repo-content-turbo-frame" href="https://github.com/reyashv/python"><span>python</span></a></span></span><span class="separator">/</span><strong class="final-path">tkinterproject.py</strong>
      <span class="separator">/</span><details class="details-reset details-overlay d-inline" id="jumpto-symbol-select-menu">
    <summary aria-haspopup="menu" data-hotkey="r" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.click_on_blob_definitions&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;click_on_blob_definitions&quot;,&quot;repository_id&quot;:572068788,&quot;ref&quot;:&quot;main&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;backend&quot;:&quot;ALEPH_FUZZY&quot;,&quot;code_nav_context&quot;:&quot;BLOB_VIEW&quot;,&quot;retry_backend&quot;:&quot;&quot;,&quot;cross_repo_results_included&quot;:&quot;CROSS_REPO_UNKNOWN&quot;,&quot;in_repo_result_count&quot;:0,&quot;cross_repo_result_count&quot;:0,&quot;originating_url&quot;:&quot;https://github.com/reyashv/python/blob/main/tkinterproject.py&quot;,&quot;user_id&quot;:124596951}}" data-hydro-click-hmac="5f9a55fe68c7e0d4d9be66102bc0945ce1d461b219ff2646e5d257c820b7f122" data-view-component="true" class="Link--secondary css-truncate btn-link" role="button">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-code">
    <path fill-rule="evenodd" d="M4.72 3.22a.75.75 0 011.06 1.06L2.06 8l3.72 3.72a.75.75 0 11-1.06 1.06L.47 8.53a.75.75 0 010-1.06l4.25-4.25zm6.56 0a.75.75 0 10-1.06 1.06L13.94 8l-3.72 3.72a.75.75 0 101.06 1.06l4.25-4.25a.75.75 0 000-1.06l-4.25-4.25z"></path>
</svg>
    <span data-menu-button="">Jump to</span>
    <span class="dropdown-caret"></span>
</summary>  <details-menu class="SelectMenu SelectMenu--hasFilter" role="menu" data-focus-trap="suspended"><span class="sentinel" tabindex="0" aria-hidden="true"></span>
    <div class="SelectMenu-modal">
      <header class="SelectMenu-header">
        <span class="SelectMenu-title">Code definitions</span>
        <button class="SelectMenu-closeButton" type="button" data-toggle-for="jumpto-symbol-select-menu">
          <svg aria-label="Close menu" role="img" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path fill-rule="evenodd" d="M3.72 3.72a.75.75 0 011.06 0L8 6.94l3.22-3.22a.75.75 0 111.06 1.06L9.06 8l3.22 3.22a.75.75 0 11-1.06 1.06L8 9.06l-3.22 3.22a.75.75 0 01-1.06-1.06L6.94 8 3.72 4.78a.75.75 0 010-1.06z"></path>
</svg>
        </button>
      </header>
      <div class="SelectMenu-list">
          <div class="SelectMenu-blankslate">
            <p class="mb-0 color-fg-muted">
              No definitions found in this file.
            </p>
          </div>
        <div data-filterable-for="jumpto-symbols-filter-field" data-filterable-type="substring">
        </div>
      </div>
      <footer class="SelectMenu-footer">
        <div class="d-flex flex-justify-between">
          Code navigation not available for this commit
          <svg class="octicon octicon-dot-fill text-light-gray" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 4a4 4 0 100 8 4 4 0 000-8z"></path></svg>
        </div>
      </footer>
    </div>
  <span class="sentinel" tabindex="0" aria-hidden="true"></span></details-menu>
</details>

  </h2>
    <a href="https://github.com/reyashv/python/find/main" data-pjax="" data-hotkey="t" data-view-component="true" class="btn mr-2 d-none d-md-block">    Go to file
</a>
  <details id="blob-more-options-details" data-view-component="true" class="details-overlay details-reset position-relative">
    <summary role="button" data-view-component="true" class="btn">    <svg aria-label="More options" role="img" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-kebab-horizontal">
    <path d="M8 9a1.5 1.5 0 100-3 1.5 1.5 0 000 3zM1.5 9a1.5 1.5 0 100-3 1.5 1.5 0 000 3zm13 0a1.5 1.5 0 100-3 1.5 1.5 0 000 3z"></path>
</svg>
</summary>
  <div data-view-component="true">      <ul class="dropdown-menu dropdown-menu-sw">
        <li class="d-block d-md-none">
          <a class="dropdown-item d-flex flex-items-baseline" data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;FIND_FILE_BUTTON&quot;,&quot;repository_id&quot;:572068788,&quot;originating_url&quot;:&quot;https://github.com/reyashv/python/blob/main/tkinterproject.py&quot;,&quot;user_id&quot;:124596951}}" data-hydro-click-hmac="44c47e1adda455fda1e8aef7266d3cd68d52b7fd3950f2c3632c2feb59620c8d" data-ga-click="Repository, find file, location:repo overview" data-hotkey="t" href="https://github.com/reyashv/python/find/main">
            <span class="flex-auto">Go to file</span>
            <span class="text-small color-fg-muted" aria-hidden="true">T</span>
</a>        </li>
        <li data-toggle-for="blob-more-options-details">
            <button data-toggle-for="jumpto-line-details-dialog" type="button" data-view-component="true" class="dropdown-item btn-link">    <span class="d-flex flex-items-baseline">
              <span class="flex-auto">Go to line</span>
              <span class="text-small color-fg-muted" aria-hidden="true">L</span>
            </span>
</button>        </li>
        <li data-toggle-for="blob-more-options-details">
            <button data-toggle-for="jumpto-symbol-select-menu" type="button" data-view-component="true" class="dropdown-item btn-link">    <span class="d-flex flex-items-baseline">
              <span class="flex-auto">Go to definition</span>
              <span class="text-small color-fg-muted" aria-hidden="true">R</span>
            </span>
</button>        </li>
        <li class="dropdown-divider" role="none"></li>
        <li>
          <clipboard-copy data-toggle-for="blob-more-options-details" aria-label="Copy path" value="tkinterproject.py" data-view-component="true" class="dropdown-item cursor-pointer" tabindex="0" role="button">
    
            Copy path

</clipboard-copy>        </li>
        <li>
          <clipboard-copy data-toggle-for="blob-more-options-details" aria-label="Copy permalink" value="https://github.com/reyashv/python/blob/6896039a3a2afc5582fe93390554dd72d0023ef8/tkinterproject.py" data-view-component="true" class="dropdown-item cursor-pointer" tabindex="0" role="button">
    
            <span class="d-flex flex-items-baseline">
              <span class="flex-auto">Copy permalink</span>
            </span>

</clipboard-copy>        </li>
      </ul>
</div>
</details></div>





    <div id="spoof-warning" class="mt-0 pb-3" hidden="" aria-hidden="">
  <div data-view-component="true" class="flash flash-warn mt-0 clearfix">
  
  
    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert float-left mt-1">
    <path fill-rule="evenodd" d="M8.22 1.754a.25.25 0 00-.44 0L1.698 13.132a.25.25 0 00.22.368h12.164a.25.25 0 00.22-.368L8.22 1.754zm-1.763-.707c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0114.082 15H1.918a1.75 1.75 0 01-1.543-2.575L6.457 1.047zM9 11a1 1 0 11-2 0 1 1 0 012 0zm-.25-5.25a.75.75 0 00-1.5 0v2.5a.75.75 0 001.5 0v-2.5z"></path>
</svg>

      <div class="overflow-hidden">This commit does not belong to any branch on this repository, and may belong to a fork outside of the repository.</div>


  
</div></div>

    



    <div class="Box d-flex flex-column flex-shrink-0 mb-3">
  

  <div class="Box-header Details js-details-container">
      <div class="d-flex flex-items-center">
        <span class="flex-shrink-0 ml-n1 mr-n1 mt-n1 mb-n1">
          <a rel="author" data-hovercard-type="user" data-hovercard-url="/users/reyashv/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/reyashv"><img class="avatar avatar-user" src="./tinker_ui_files/97713189" width="24" height="24" alt="@reyashv"></a>
        </span>
        <div class="flex-1 d-flex flex-items-center ml-3 min-width-0">
          <div class="css-truncate css-truncate-overflow">
            <a class="text-bold Link--primary" rel="author" data-hovercard-type="user" data-hovercard-url="/users/reyashv/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/reyashv">reyashv</a>

              <span class="markdown-title">
                <a data-pjax="true" title="Add files via upload" class="Link--secondary" href="https://github.com/reyashv/python/commit/6896039a3a2afc5582fe93390554dd72d0023ef8">Add files via upload</a>
              </span>
          </div>


          <span class="ml-2">
            
          </span>
        </div>
        <div class="ml-3 d-flex flex-shrink-0 flex-items-center flex-justify-end color-fg-muted no-wrap">
          <span class="d-none d-md-inline">
            <span>Latest commit</span>
            <a class="text-small text-mono Link--secondary" href="https://github.com/reyashv/python/commit/6896039a3a2afc5582fe93390554dd72d0023ef8" data-pjax="">6896039</a>
            <span itemprop="dateModified"><relative-time datetime="2022-11-29T13:48:36Z" class="no-wrap" title="Nov 29, 2022, 7:18 PM GMT+5:30">Nov 29, 2022</relative-time></span>
          </span>

          <a data-pjax="" href="https://github.com/reyashv/python/commits/main/tkinterproject.py" class="ml-3 no-wrap Link--primary no-underline">
            <svg text="gray" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-history">
    <path fill-rule="evenodd" d="M1.643 3.143L.427 1.927A.25.25 0 000 2.104V5.75c0 .138.112.25.25.25h3.646a.25.25 0 00.177-.427L2.715 4.215a6.5 6.5 0 11-1.18 4.458.75.75 0 10-1.493.154 8.001 8.001 0 101.6-5.684zM7.75 4a.75.75 0 01.75.75v2.992l2.028.812a.75.75 0 01-.557 1.392l-2.5-1A.75.75 0 017 8.25v-3.5A.75.75 0 017.75 4z"></path>
</svg>
            <span class="d-none d-sm-inline">
              <strong>History</strong>
            </span>
          </a>
        </div>
      </div>

  </div>

  <div class="Box-body d-flex flex-items-center flex-auto border-bottom-0 flex-wrap">
    <details class="details-reset details-overlay details-overlay-dark lh-default color-fg-default float-left mr-3" id="blob_contributors_box">
      <summary class="Link--primary" role="button">
        <svg text="gray" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-people">
    <path fill-rule="evenodd" d="M5.5 3.5a2 2 0 100 4 2 2 0 000-4zM2 5.5a3.5 3.5 0 115.898 2.549 5.507 5.507 0 013.034 4.084.75.75 0 11-1.482.235 4.001 4.001 0 00-7.9 0 .75.75 0 01-1.482-.236A5.507 5.507 0 013.102 8.05 3.49 3.49 0 012 5.5zM11 4a.75.75 0 100 1.5 1.5 1.5 0 01.666 2.844.75.75 0 00-.416.672v.352a.75.75 0 00.574.73c1.2.289 2.162 1.2 2.522 2.372a.75.75 0 101.434-.44 5.01 5.01 0 00-2.56-3.012A3 3 0 0011 4z"></path>
</svg>
        <strong>1</strong>
        
        contributor
      </summary>
      <details-dialog class="Box Box--overlay d-flex flex-column anim-fade-in fast" aria-label="Users who have contributed to this file" src="/reyashv/python/contributors-list/main/tkinterproject.py" preload="" role="dialog" aria-modal="true">
        <div class="Box-header">
          <button class="Box-btn-octicon btn-octicon float-right" type="button" aria-label="Close dialog" data-close-dialog="">
            <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path fill-rule="evenodd" d="M3.72 3.72a.75.75 0 011.06 0L8 6.94l3.22-3.22a.75.75 0 111.06 1.06L9.06 8l3.22 3.22a.75.75 0 11-1.06 1.06L8 9.06l-3.22 3.22a.75.75 0 01-1.06-1.06L6.94 8 3.72 4.78a.75.75 0 010-1.06z"></path>
</svg>
          </button>
          <h3 class="Box-title">
            Users who have contributed to this file
          </h3>
        </div>
        <include-fragment>
          <svg style="box-sizing: content-box; color: var(--color-icon-primary);" width="32" height="32" viewBox="0 0 16 16" fill="none" data-view-component="true" class="my-3 mx-auto d-block anim-rotate">
  <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke"></circle>
  <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke"></path>
</svg>
        </include-fragment>
      </details-dialog>
    </details>
  </div>
</div>



      








  
    <div data-target="readme-toc.content" class="Box mt-3 position-relative">
      
  <div class="Box-header js-blob-header py-2 pr-2 d-flex flex-shrink-0 flex-md-row flex-items-center">


  <div class="text-mono f6 flex-auto pr-3 flex-order-2 flex-md-order-1">

      860 lines (765 sloc)
      <span class="file-info-divider"></span>
    31.9 KB
  </div>

  <div class="d-flex py-1 py-md-0 flex-auto flex-order-1 flex-md-order-2 flex-sm-grow-0 flex-justify-between hide-sm hide-md">
      

    <div class="BtnGroup">
        <a data-permalink-href="/reyashv/python/raw/6896039a3a2afc5582fe93390554dd72d0023ef8/tkinterproject.py" href="https://github.com/reyashv/python/raw/main/tkinterproject.py" id="raw-url" data-view-component="true" class="js-permalink-replaceable-link btn-sm btn BtnGroup-item">    Raw
</a>          <a data-permalink-href="/reyashv/python/blame/6896039a3a2afc5582fe93390554dd72d0023ef8/tkinterproject.py" href="https://github.com/reyashv/python/blame/main/tkinterproject.py" data-hotkey="b" data-view-component="true" class="js-update-url-with-hash js-permalink-replaceable-link btn-sm btn BtnGroup-item">    Blame
</a>    </div>

    <div class="d-flex">
        
<div class="ml-1">
  <!-- '"` --><!-- </textarea></xmp> --><form class="BtnGroup-parent js-update-url-with-hash " data-turbo="false" action="https://github.com/reyashv/python/edit/main/tkinterproject.py" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="X6GwNDGQVZj3XU0CCWQ0IwMsccwf1ZwmE5gE3kYSv7tEd1wjVHlWINV1lKf-DTTiRjUkLe8553bRqFebkq0Eiw" autocomplete="off">
      <button title="Edit this file" data-hotkey="e" data-disable-with="" type="submit" data-view-component="true" class="btn-sm BtnGroup-item btn">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-pencil">
    <path fill-rule="evenodd" d="M11.013 1.427a1.75 1.75 0 012.474 0l1.086 1.086a1.75 1.75 0 010 2.474l-8.61 8.61c-.21.21-.47.364-.756.445l-3.251.93a.75.75 0 01-.927-.928l.929-3.25a1.75 1.75 0 01.445-.758l8.61-8.61zm1.414 1.06a.25.25 0 00-.354 0L10.811 3.75l1.439 1.44 1.263-1.263a.25.25 0 000-.354l-1.086-1.086zM11.189 6.25L9.75 4.81l-6.286 6.287a.25.25 0 00-.064.108l-.558 1.953 1.953-.558a.249.249 0 00.108-.064l6.286-6.286z"></path>
</svg>
</button></form>
  <details class="details-reset details-overlay select-menu BtnGroup-parent d-inline-block position-relative">
      <summary data-disable-invalid="" data-disable-with="" data-dropdown-tracking="{&quot;type&quot;:&quot;blob_edit_dropdown.more_options_click&quot;,&quot;context&quot;:{&quot;repository_id&quot;:572068788,&quot;actor_id&quot;:124596951,&quot;github_dev_enabled&quot;:true,&quot;edit_enabled&quot;:true,&quot;small_screen&quot;:false}}" aria-label="Select additional options" data-view-component="true" class="js-blob-dropdown-click select-menu-button btn-sm btn BtnGroup-item float-none px-2">
</summary>    <div class="SelectMenu right-0">
      <div class="SelectMenu-modal width-full">
        <div class="SelectMenu-list SelectMenu-list--borderless py-2">
          <!-- '"` --><!-- </textarea></xmp> --><form class="SelectMenu-item js-update-url-with-hash " data-turbo="false" action="https://github.com/reyashv/python/edit/main/tkinterproject.py" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="Lo-TwtmUGx2OTvAOnPdH2zO5dX2bwZBrgYhLQj157RU1WX_VvH0YpaxmKatrnkcadqAgnGst6ztDuBgH6cZWJQ" autocomplete="off">
              <button title="Edit this file" type="submit" data-view-component="true" class="btn-invisible btn width-full d-flex flex-justify-between color-fg-default text-normal p-0">    <div class="mr-5">Edit this file</div>
              <div class="color-fg-muted">E</div>
</button></form>
            <a aria-label="Open this file in github.dev" data-dropdown-tracking="{&quot;type&quot;:&quot;blob_edit_dropdown.dev_link_click&quot;,&quot;context&quot;:{&quot;repository_id&quot;:572068788,&quot;actor_id&quot;:124596951,&quot;edit_enabled&quot;:true,&quot;small_screen&quot;:false}}" href="https://github.dev/" data-view-component="true" class="SelectMenu-item js-github-dev-shortcut js-blob-dropdown-click width-full d-flex flex-justify-between color-fg-default f5 text-normal">
              <div class="mr-5 no-wrap">Open in github.dev</div>
              <div class="color-fg-muted">.</div>
</a>
            <a data-platforms="windows,mac" aria-label="Open this file in GitHub Desktop" href="https://desktop.github.com/" data-view-component="true" class="SelectMenu-item no-wrap js-remove-unless-platform width-full text-normal color-fg-default f5">
              Open in GitHub Desktop
</a>        </div>
      </div>
    </div>
  </details>
</div>


        
<div>
  <remote-clipboard-copy class="d-inline-block btn-octicon" style="height: 26px" data-src="/reyashv/python/raw/6896039a3a2afc5582fe93390554dd72d0023ef8/tkinterproject.py" data-action="click:remote-clipboard-copy#remoteCopy" data-state-timeout="2000" data-catalyst="">
  

  <span data-target="remote-clipboard-copy.idle">      <span class="tooltipped tooltipped-nw cursor-pointer" data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;COPY_RAW_CONTENTS_BUTTON&quot;,&quot;repository_id&quot;:572068788,&quot;originating_url&quot;:&quot;https://github.com/reyashv/python/blob/main/tkinterproject.py&quot;,&quot;user_id&quot;:124596951}}" data-hydro-click-hmac="3f34ced25534a066c749dc2df988a394f5630e3e46435ebd2468682d596370ae" aria-label="Copy raw contents">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy">
    <path fill-rule="evenodd" d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 010 1.5h-1.5a.25.25 0 00-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 00.25-.25v-1.5a.75.75 0 011.5 0v1.5A1.75 1.75 0 019.25 16h-7.5A1.75 1.75 0 010 14.25v-7.5z"></path><path fill-rule="evenodd" d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0114.25 11h-7.5A1.75 1.75 0 015 9.25v-7.5zm1.75-.25a.25.25 0 00-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 00.25-.25v-7.5a.25.25 0 00-.25-.25h-7.5z"></path>
</svg>
</span></span>
  <span data-target="remote-clipboard-copy.fetching" hidden="">      <svg style="box-sizing: content-box; color: var(--color-icon-primary);" width="16" height="16" viewBox="0 0 16 16" fill="none" data-view-component="true" class="anim-rotate">
  <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke"></circle>
  <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke"></path>
</svg>
</span>
  <span data-target="remote-clipboard-copy.success" hidden="">      <span class="tooltipped tooltipped-nw" aria-label="Copied!">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check color-fg-success">
    <path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"></path>
</svg>
      </span>
</span>
  <span data-target="remote-clipboard-copy.error" hidden="">      <span class="tooltipped tooltipped-nw" aria-label="Something went wrong. Try again.">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert color-fg-attention">
    <path fill-rule="evenodd" d="M8.22 1.754a.25.25 0 00-.44 0L1.698 13.132a.25.25 0 00.22.368h12.164a.25.25 0 00.22-.368L8.22 1.754zm-1.763-.707c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0114.082 15H1.918a1.75 1.75 0 01-1.543-2.575L6.457 1.047zM9 11a1 1 0 11-2 0 1 1 0 012 0zm-.25-5.25a.75.75 0 00-1.5 0v2.5a.75.75 0 001.5 0v-2.5z"></path>
</svg>
      </span>
</span>
</remote-clipboard-copy></div>


          <!-- '"` --><!-- </textarea></xmp> --><form class="inline-form" data-turbo="false" action="https://github.com/reyashv/python/delete/main/tkinterproject.py" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="L7M5XAjrfmZBIVIzvw3B_hiA9l8e7dHKDHYcbJkEe2Kf5i5yXJxHYTKupnrE57JouDNJRLt0Pm2WZrJoL0CL8A">
            <button class="btn-octicon btn-octicon-danger tooltipped tooltipped-nw" type="submit" aria-label="Delete this file" data-disable-with="">
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-trash">
    <path fill-rule="evenodd" d="M6.5 1.75a.25.25 0 01.25-.25h2.5a.25.25 0 01.25.25V3h-3V1.75zm4.5 0V3h2.25a.75.75 0 010 1.5H2.75a.75.75 0 010-1.5H5V1.75C5 .784 5.784 0 6.75 0h2.5C10.216 0 11 .784 11 1.75zM4.496 6.675a.75.75 0 10-1.492.15l.66 6.6A1.75 1.75 0 005.405 15h5.19c.9 0 1.652-.681 1.741-1.576l.66-6.6a.75.75 0 00-1.492-.149l-.66 6.6a.25.25 0 01-.249.225h-5.19a.25.25 0 01-.249-.225l-.66-6.6z"></path>
</svg>
            </button>
</form>    </div>
  </div>

    <div class="d-flex hide-lg hide-xl flex-order-2 flex-grow-0">
      <details class="dropdown details-reset details-overlay d-inline-block">
        <summary class="js-blob-dropdown-click btn-octicon" aria-haspopup="true" aria-label="possible actions" data-dropdown-tracking="{&quot;type&quot;:&quot;blob_edit_dropdown.more_options_click&quot;,&quot;context&quot;:{&quot;repository_id&quot;:572068788,&quot;actor_id&quot;:124596951,&quot;github_dev_enabled&quot;:true,&quot;edit_enabled&quot;:true,&quot;small_screen&quot;:true}}">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-kebab-horizontal">
    <path d="M8 9a1.5 1.5 0 100-3 1.5 1.5 0 000 3zM1.5 9a1.5 1.5 0 100-3 1.5 1.5 0 000 3zm13 0a1.5 1.5 0 100-3 1.5 1.5 0 000 3z"></path>
</svg>
        </summary>

        <ul class="dropdown-menu dropdown-menu-sw" style="width: 175px">
            <li>
                <a class="dropdown-item tooltipped tooltipped-nw js-remove-unless-platform" data-platforms="windows,mac" href="https://desktop.github.com/">
                  Open with Desktop
                </a>
            </li>
          <li>
            <a class="dropdown-item" href="https://github.com/reyashv/python/raw/main/tkinterproject.py">
              View raw
            </a>
          </li>
            <li>
              <remote-clipboard-copy class="dropdown-item" data-src="/reyashv/python/raw/main/tkinterproject.py" data-action="click:remote-clipboard-copy#remoteCopy" data-state-timeout="2000" data-catalyst="">
  

  <span data-target="remote-clipboard-copy.idle">                  <span class="cursor-pointer" data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;COPY_RAW_CONTENTS_BUTTON&quot;,&quot;repository_id&quot;:572068788,&quot;originating_url&quot;:&quot;https://github.com/reyashv/python/blob/main/tkinterproject.py&quot;,&quot;user_id&quot;:124596951}}" data-hydro-click-hmac="3f34ced25534a066c749dc2df988a394f5630e3e46435ebd2468682d596370ae">
                    Copy raw contents
</span></span>
  <span data-target="remote-clipboard-copy.fetching" hidden="">                  Copy raw contents
                  <span class="d-inline-block position-relative" style="top: 3px">
                    <svg aria-label="fetching contents…" style="box-sizing: content-box; color: var(--color-icon-primary);" width="16" height="16" viewBox="0 0 16 16" fill="none" data-view-component="true" class="anim-rotate">
  <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke"></circle>
  <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke"></path>
</svg>
                  </span>
</span>
  <span data-target="remote-clipboard-copy.success" hidden="">                  Copy raw contents
                  <svg aria-label="Copied!" role="img" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check color-fg-success">
    <path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"></path>
</svg>
</span>
  <span data-target="remote-clipboard-copy.error" hidden="">                  Copy raw contents
                  <svg aria-label="Something went wrong. Try again." role="img" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert color-fg-attention">
    <path fill-rule="evenodd" d="M8.22 1.754a.25.25 0 00-.44 0L1.698 13.132a.25.25 0 00.22.368h12.164a.25.25 0 00.22-.368L8.22 1.754zm-1.763-.707c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0114.082 15H1.918a1.75 1.75 0 01-1.543-2.575L6.457 1.047zM9 11a1 1 0 11-2 0 1 1 0 012 0zm-.25-5.25a.75.75 0 00-1.5 0v2.5a.75.75 0 001.5 0v-2.5z"></path>
</svg>
</span>
</remote-clipboard-copy>            </li>
            <li>
              <a class="dropdown-item" href="https://github.com/reyashv/python/blame/main/tkinterproject.py">
                View blame
              </a>
            </li>

              <li class="dropdown-divider" role="none"></li>
              <li>
                <a class="dropdown-item" href="https://github.com/reyashv/python/edit/main/tkinterproject.py">Edit file</a>
              </li>
                <li>
                  <a data-dropdown-tracking="{&quot;type&quot;:&quot;blob_edit_dropdown.dev_link_click&quot;,&quot;context&quot;:{&quot;repository_id&quot;:572068788,&quot;actor_id&quot;:124596951,&quot;edit_enabled&quot;:true,&quot;small_screen&quot;:true}}" href="https://github.dev/" data-view-component="true" class="dropdown-item js-github-dev-shortcut js-blob-dropdown-click">Open with github.dev</a>
                </li>
              <li>
                <a class="dropdown-item menu-item-danger" href="https://github.com/reyashv/python/delete/main/tkinterproject.py">Delete file</a>
              </li>
        </ul>
      </details>
    </div>
</div>


      
    <div itemprop="text" class="Box-body p-0 blob-wrapper data type-python  gist-border-0">

        
<div class="js-blob-code-container blob-code-content">

  <template class="js-file-alert-template"></template>
<template class="js-line-alert-template"></template>

  <table data-hpc="" class="highlight tab-size js-file-line-container js-code-nav-container js-tagsearch-file" data-tab-size="8" data-paste-markdown-skip="" data-tagsearch-lang="Python" data-tagsearch-path="tkinterproject.py">
        <tbody><tr>
          <td id="L1" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="1"></td>
          <td id="LC1" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> <span class="pl-s1">json</span></td>
        </tr>
        <tr>
          <td id="L2" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="2"></td>
          <td id="LC2" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> <span class="pl-s1">tkinter</span> <span class="pl-k">import</span> <span class="pl-c1">*</span></td>
        </tr>
        <tr>
          <td id="L3" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="3"></td>
          <td id="LC3" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> <span class="pl-s1">datetime</span> <span class="pl-k">import</span> <span class="pl-s1">datetime</span></td>
        </tr>
        <tr>
          <td id="L4" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="4"></td>
          <td id="LC4" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> <span class="pl-s1">functools</span> <span class="pl-k">import</span> <span class="pl-s1">partial</span></td>
        </tr>
        <tr>
          <td id="L5" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="5"></td>
          <td id="LC5" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> <span class="pl-v">PIL</span> <span class="pl-k">import</span> <span class="pl-v">ImageTk</span>,<span class="pl-v">Image</span></td>
        </tr>
        <tr>
          <td id="L6" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="6"></td>
          <td id="LC6" class="blob-code blob-code-inner js-file-line"><span class="pl-s1">booking</span><span class="pl-c1">=</span>{}</td>
        </tr>
        <tr>
          <td id="L7" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="7"></td>
          <td id="LC7" class="blob-code blob-code-inner js-file-line">
</td>
        </tr>
        <tr>
          <td id="L8" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="8"></td>
          <td id="LC8" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">bill</span>():</td>
        </tr>
        <tr>
          <td id="L9" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="9"></td>
          <td id="LC9" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">with</span> <span class="pl-en">open</span>(<span class="pl-s">'bookings.json'</span>,<span class="pl-s">'r'</span>) <span class="pl-k">as</span> <span class="pl-s1">file</span>:</td>
        </tr>
        <tr>
          <td id="L10" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="10"></td>
          <td id="LC10" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">a</span><span class="pl-c1">=</span><span class="pl-s1">json</span>.<span class="pl-en">load</span>(<span class="pl-s1">file</span>)</td>
        </tr>
        <tr>
          <td id="L11" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="11"></td>
          <td id="LC11" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">bills</span><span class="pl-c1">=</span><span class="pl-v">Tk</span>()</td>
        </tr>
        <tr>
          <td id="L12" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="12"></td>
          <td id="LC12" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">bills</span>.<span class="pl-en">geometry</span>(<span class="pl-s">"1000x2000+10+20"</span>)</td>
        </tr>
        <tr>
          <td id="L13" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="13"></td>
          <td id="LC13" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">bills</span>.<span class="pl-en">state</span>(<span class="pl-s">"zoomed"</span>)</td>
        </tr>
        <tr>
          <td id="L14" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="14"></td>
          <td id="LC14" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">bills</span>[<span class="pl-s">'bg'</span>]<span class="pl-c1">=</span><span class="pl-s">'deepskyblue'</span></td>
        </tr>
        <tr>
          <td id="L15" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="15"></td>
          <td id="LC15" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">heading</span> <span class="pl-c1">=</span> <span class="pl-v">Label</span>(<span class="pl-s1">bills</span>,<span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s">"Ticket Confirmation"</span>,<span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">'verdana'</span>,<span class="pl-c1">25</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"black"</span>,<span class="pl-s1">bg</span><span class="pl-c1">=</span><span class="pl-s">"deepskyblue"</span>)</td>
        </tr>
        <tr>
          <td id="L16" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="16"></td>
          <td id="LC16" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">heading</span>.<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">10</span>)</td>
        </tr>
        <tr>
          <td id="L17" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="17"></td>
          <td id="LC17" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">style1</span> <span class="pl-c1">=</span> <span class="pl-v">Label</span>(<span class="pl-s1">bills</span>,<span class="pl-s1">bg</span><span class="pl-c1">=</span><span class="pl-s">"black"</span>,<span class="pl-s1">height</span><span class="pl-c1">=</span><span class="pl-c1">1</span>,<span class="pl-s1">width</span><span class="pl-c1">=</span><span class="pl-c1">500</span>)</td>
        </tr>
        <tr>
          <td id="L18" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="18"></td>
          <td id="LC18" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">style1</span>.<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">10</span>)</td>
        </tr>
        <tr>
          <td id="L19" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="19"></td>
          <td id="LC19" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-s1">a</span>:</td>
        </tr>
        <tr>
          <td id="L20" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="20"></td>
          <td id="LC20" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">label</span> <span class="pl-c1">=</span> <span class="pl-v">Label</span>(<span class="pl-s1">bills</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span>(<span class="pl-s1">i</span><span class="pl-c1">+</span><span class="pl-s">" : "</span><span class="pl-c1">+</span><span class="pl-s1">a</span>[<span class="pl-s1">i</span>]), <span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"Black"</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">"verdana"</span>,<span class="pl-c1">16</span>,<span class="pl-s">'bold'</span>))</td>
        </tr>
        <tr>
          <td id="L21" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="21"></td>
          <td id="LC21" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">label</span>.<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">16</span>)</td>
        </tr>
        <tr>
          <td id="L22" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="22"></td>
          <td id="LC22" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">label1</span><span class="pl-c1">=</span><span class="pl-v">Label</span>(<span class="pl-s1">bills</span>,<span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s">"Thanks for booking!!"</span>, <span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"Black"</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">"verdana"</span>,<span class="pl-c1">16</span>,<span class="pl-s">'bold'</span>))</td>
        </tr>
        <tr>
          <td id="L23" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="23"></td>
          <td id="LC23" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">label1</span>.<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">16</span>)</td>
        </tr>
        <tr>
          <td id="L24" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="24"></td>
          <td id="LC24" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">bills</span>.<span class="pl-en">mainloop</span>()</td>
        </tr>
        <tr>
          <td id="L25" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="25"></td>
          <td id="LC25" class="blob-code blob-code-inner js-file-line">
</td>
        </tr>
        <tr>
          <td id="L26" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="26"></td>
          <td id="LC26" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">seats</span>(<span class="pl-s1">i</span>):</td>
        </tr>
        <tr>
          <td id="L27" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="27"></td>
          <td id="LC27" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">booking</span>[<span class="pl-s">'Time'</span>]<span class="pl-c1">=</span><span class="pl-s1">i</span></td>
        </tr>
        <tr>
          <td id="L28" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="28"></td>
          <td id="LC28" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">with</span> <span class="pl-en">open</span>(<span class="pl-s">'bookings.json'</span>,<span class="pl-s">'w'</span>) <span class="pl-k">as</span> <span class="pl-s1">file</span>:</td>
        </tr>
        <tr>
          <td id="L29" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="29"></td>
          <td id="LC29" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">json</span>.<span class="pl-en">dump</span>(<span class="pl-s1">booking</span>,<span class="pl-s1">file</span>)</td>
        </tr>
        <tr>
          <td id="L30" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="30"></td>
          <td id="LC30" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">receive</span>():</td>
        </tr>
        <tr>
          <td id="L31" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="31"></td>
          <td id="LC31" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">z</span><span class="pl-c1">=</span><span class="pl-s1">enter</span>.<span class="pl-en">get</span>()</td>
        </tr>
        <tr>
          <td id="L32" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="32"></td>
          <td id="LC32" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">booking</span>[<span class="pl-s">'Number of Seats'</span>]<span class="pl-c1">=</span><span class="pl-s1">z</span></td>
        </tr>
        <tr>
          <td id="L33" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="33"></td>
          <td id="LC33" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">booking</span>[<span class="pl-s">'Total cost'</span>]<span class="pl-c1">=</span><span class="pl-en">str</span>(<span class="pl-en">int</span>(<span class="pl-s1">z</span>)<span class="pl-c1">*</span><span class="pl-c1">150</span>)</td>
        </tr>
        <tr>
          <td id="L34" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="34"></td>
          <td id="LC34" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">with</span> <span class="pl-en">open</span>(<span class="pl-s">'bookings.json'</span>,<span class="pl-s">'w'</span>) <span class="pl-k">as</span> <span class="pl-s1">file</span>:</td>
        </tr>
        <tr>
          <td id="L35" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="35"></td>
          <td id="LC35" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">json</span>.<span class="pl-en">dump</span>(<span class="pl-s1">booking</span>,<span class="pl-s1">file</span>)</td>
        </tr>
        <tr>
          <td id="L36" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="36"></td>
          <td id="LC36" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">file</span>.<span class="pl-en">close</span>()</td>
        </tr>
        <tr>
          <td id="L37" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="37"></td>
          <td id="LC37" class="blob-code blob-code-inner js-file-line">        <span class="pl-en">bill</span>()</td>
        </tr>
        <tr>
          <td id="L38" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="38"></td>
          <td id="LC38" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">seats</span><span class="pl-c1">=</span><span class="pl-v">Tk</span>()</td>
        </tr>
        <tr>
          <td id="L39" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="39"></td>
          <td id="LC39" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">seats</span>.<span class="pl-en">geometry</span>(<span class="pl-s">"1000x2000+10+20"</span>)</td>
        </tr>
        <tr>
          <td id="L40" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="40"></td>
          <td id="LC40" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">seats</span>.<span class="pl-en">state</span>(<span class="pl-s">"zoomed"</span>)</td>
        </tr>
        <tr>
          <td id="L41" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="41"></td>
          <td id="LC41" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">seats</span>[<span class="pl-s">'bg'</span>]<span class="pl-c1">=</span><span class="pl-s">'deepskyblue'</span></td>
        </tr>
        <tr>
          <td id="L42" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="42"></td>
          <td id="LC42" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">heading</span> <span class="pl-c1">=</span> <span class="pl-v">Label</span>(<span class="pl-s1">seats</span>,<span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s">"SEATS"</span>,<span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">'verdana'</span>,<span class="pl-c1">25</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"black"</span>,<span class="pl-s1">bg</span><span class="pl-c1">=</span><span class="pl-s">"deepskyblue"</span>)</td>
        </tr>
        <tr>
          <td id="L43" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="43"></td>
          <td id="LC43" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">heading</span>.<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">10</span>)</td>
        </tr>
        <tr>
          <td id="L44" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="44"></td>
          <td id="LC44" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">style1</span> <span class="pl-c1">=</span> <span class="pl-v">Label</span>(<span class="pl-s1">seats</span>,<span class="pl-s1">bg</span><span class="pl-c1">=</span><span class="pl-s">"black"</span>,<span class="pl-s1">height</span><span class="pl-c1">=</span><span class="pl-c1">1</span>,<span class="pl-s1">width</span><span class="pl-c1">=</span><span class="pl-c1">500</span>)</td>
        </tr>
        <tr>
          <td id="L45" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="45"></td>
          <td id="LC45" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">style1</span>.<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">10</span>)</td>
        </tr>
        <tr>
          <td id="L46" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="46"></td>
          <td id="LC46" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">name</span> <span class="pl-c1">=</span> <span class="pl-v">Label</span>(<span class="pl-s1">seats</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s">"Enter number of seats"</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">'arial'</span>,<span class="pl-c1">30</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"deepskyblue"</span>,<span class="pl-s1">bg</span><span class="pl-c1">=</span><span class="pl-s">"black"</span>)</td>
        </tr>
        <tr>
          <td id="L47" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="47"></td>
          <td id="LC47" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">name</span>.<span class="pl-en">place</span>(<span class="pl-s1">x</span><span class="pl-c1">=</span><span class="pl-c1">600</span>,<span class="pl-s1">y</span><span class="pl-c1">=</span><span class="pl-c1">150</span>)</td>
        </tr>
        <tr>
          <td id="L48" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="48"></td>
          <td id="LC48" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">enter</span> <span class="pl-c1">=</span> <span class="pl-v">Entry</span>(<span class="pl-s1">seats</span>, <span class="pl-s1">bd</span> <span class="pl-c1">=</span> <span class="pl-c1">5</span>,<span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"black"</span>)</td>
        </tr>
        <tr>
          <td id="L49" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="49"></td>
          <td id="LC49" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">enter</span>.<span class="pl-en">place</span>(<span class="pl-s1">x</span><span class="pl-c1">=</span><span class="pl-c1">600</span>,<span class="pl-s1">y</span><span class="pl-c1">=</span><span class="pl-c1">230</span>)</td>
        </tr>
        <tr>
          <td id="L50" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="50"></td>
          <td id="LC50" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">okButton</span> <span class="pl-c1">=</span> <span class="pl-v">Button</span>(<span class="pl-s1">seats</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s">"OK"</span>, <span class="pl-s1">bd</span><span class="pl-c1">=</span><span class="pl-c1">5</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">'arial'</span>,<span class="pl-c1">25</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"white"</span>,<span class="pl-s1">bg</span><span class="pl-c1">=</span><span class="pl-s">"black"</span>,<span class="pl-s1">command</span><span class="pl-c1">=</span><span class="pl-s1">receive</span>)</td>
        </tr>
        <tr>
          <td id="L51" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="51"></td>
          <td id="LC51" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">okButton</span>.<span class="pl-en">place</span>(<span class="pl-s1">x</span><span class="pl-c1">=</span><span class="pl-c1">660</span>,<span class="pl-s1">y</span><span class="pl-c1">=</span><span class="pl-c1">300</span>)</td>
        </tr>
        <tr>
          <td id="L52" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="52"></td>
          <td id="LC52" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">seats</span>.<span class="pl-en">mainloop</span>()</td>
        </tr>
        <tr>
          <td id="L53" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="53"></td>
          <td id="LC53" class="blob-code blob-code-inner js-file-line">    </td>
        </tr>
        <tr>
          <td id="L54" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="54"></td>
          <td id="LC54" class="blob-code blob-code-inner js-file-line">
</td>
        </tr>
        <tr>
          <td id="L55" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="55"></td>
          <td id="LC55" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">vikramtimes</span>(<span class="pl-s1">num</span>,<span class="pl-s1">i</span>):</td>
        </tr>
        <tr>
          <td id="L56" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="56"></td>
          <td id="LC56" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">booking</span>[<span class="pl-s">'Theatre Name'</span>]<span class="pl-c1">=</span><span class="pl-s1">i</span></td>
        </tr>
        <tr>
          <td id="L57" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="57"></td>
          <td id="LC57" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">with</span> <span class="pl-en">open</span>(<span class="pl-s">'bookings.json'</span>,<span class="pl-s">'w'</span>) <span class="pl-k">as</span> <span class="pl-s1">file</span>:</td>
        </tr>
        <tr>
          <td id="L58" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="58"></td>
          <td id="LC58" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">json</span>.<span class="pl-en">dump</span>(<span class="pl-s1">booking</span>,<span class="pl-s1">file</span>)</td>
        </tr>
        <tr>
          <td id="L59" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="59"></td>
          <td id="LC59" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">t</span><span class="pl-c1">=</span><span class="pl-v">Tk</span>()</td>
        </tr>
        <tr>
          <td id="L60" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="60"></td>
          <td id="LC60" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">t</span>.<span class="pl-en">geometry</span>(<span class="pl-s">"1000x2000+10+20"</span>)</td>
        </tr>
        <tr>
          <td id="L61" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="61"></td>
          <td id="LC61" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">t</span>.<span class="pl-en">state</span>(<span class="pl-s">"zoomed"</span>)</td>
        </tr>
        <tr>
          <td id="L62" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="62"></td>
          <td id="LC62" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">t</span>[<span class="pl-s">'bg'</span>] <span class="pl-c1">=</span> <span class="pl-s">"deepskyblue"</span></td>
        </tr>
        <tr>
          <td id="L63" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="63"></td>
          <td id="LC63" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">heading</span> <span class="pl-c1">=</span> <span class="pl-v">Label</span>(<span class="pl-s1">t</span>,<span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s">"Timings"</span>,<span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">'verdana'</span>,<span class="pl-c1">25</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"black"</span>,<span class="pl-s1">bg</span><span class="pl-c1">=</span><span class="pl-s">"deepskyblue"</span>)</td>
        </tr>
        <tr>
          <td id="L64" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="64"></td>
          <td id="LC64" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">heading</span>.<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">10</span>)</td>
        </tr>
        <tr>
          <td id="L65" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="65"></td>
          <td id="LC65" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">style1</span> <span class="pl-c1">=</span> <span class="pl-v">Label</span>(<span class="pl-s1">t</span>,<span class="pl-s1">bg</span><span class="pl-c1">=</span><span class="pl-s">"black"</span>,<span class="pl-s1">height</span><span class="pl-c1">=</span><span class="pl-c1">1</span>,<span class="pl-s1">width</span><span class="pl-c1">=</span><span class="pl-c1">500</span>)</td>
        </tr>
        <tr>
          <td id="L66" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="66"></td>
          <td id="LC66" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">style1</span>.<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">10</span>)</td>
        </tr>
        <tr>
          <td id="L67" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="67"></td>
          <td id="LC67" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">button_dict</span><span class="pl-c1">=</span>{}</td>
        </tr>
        <tr>
          <td id="L68" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="68"></td>
          <td id="LC68" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">with</span> <span class="pl-en">open</span>(<span class="pl-s">"vikram.json"</span>,<span class="pl-s">'r'</span>) <span class="pl-k">as</span> <span class="pl-s1">file</span>:</td>
        </tr>
        <tr>
          <td id="L69" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="69"></td>
          <td id="LC69" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">a</span><span class="pl-c1">=</span><span class="pl-s1">json</span>.<span class="pl-en">load</span>(<span class="pl-s1">file</span>)</td>
        </tr>
        <tr>
          <td id="L70" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="70"></td>
          <td id="LC70" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">pls</span><span class="pl-c1">=</span>[]</td>
        </tr>
        <tr>
          <td id="L71" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="71"></td>
          <td id="LC71" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-s1">a</span>.<span class="pl-en">values</span>():</td>
        </tr>
        <tr>
          <td id="L72" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="72"></td>
          <td id="LC72" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">pls</span>.<span class="pl-en">append</span>(<span class="pl-s1">i</span>)</td>
        </tr>
        <tr>
          <td id="L73" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="73"></td>
          <td id="LC73" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span>(<span class="pl-s1">num</span><span class="pl-c1">==</span><span class="pl-c1">0</span>):</td>
        </tr>
        <tr>
          <td id="L74" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="74"></td>
          <td id="LC74" class="blob-code blob-code-inner js-file-line">       <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-s1">pls</span>[<span class="pl-c1">0</span>]:</td>
        </tr>
        <tr>
          <td id="L75" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="75"></td>
          <td id="LC75" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>] <span class="pl-c1">=</span> <span class="pl-v">Button</span>(<span class="pl-s1">t</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s1">i</span>, <span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"Black"</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">"verdana"</span>,<span class="pl-c1">16</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">command</span><span class="pl-c1">=</span><span class="pl-en">partial</span>(<span class="pl-s1">seats</span>,<span class="pl-s1">i</span>))</td>
        </tr>
        <tr>
          <td id="L76" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="76"></td>
          <td id="LC76" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>].<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">16</span>)</td>
        </tr>
        <tr>
          <td id="L77" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="77"></td>
          <td id="LC77" class="blob-code blob-code-inner js-file-line">    </td>
        </tr>
        <tr>
          <td id="L78" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="78"></td>
          <td id="LC78" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span>(<span class="pl-s1">num</span><span class="pl-c1">==</span><span class="pl-c1">1</span>):</td>
        </tr>
        <tr>
          <td id="L79" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="79"></td>
          <td id="LC79" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-s1">pls</span>[<span class="pl-c1">1</span>]:</td>
        </tr>
        <tr>
          <td id="L80" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="80"></td>
          <td id="LC80" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>] <span class="pl-c1">=</span> <span class="pl-v">Button</span>(<span class="pl-s1">t</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s1">i</span>, <span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"Black"</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">"verdana"</span>,<span class="pl-c1">16</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">command</span><span class="pl-c1">=</span><span class="pl-en">partial</span>(<span class="pl-s1">seats</span>,<span class="pl-s1">i</span>))</td>
        </tr>
        <tr>
          <td id="L81" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="81"></td>
          <td id="LC81" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>].<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">16</span>)</td>
        </tr>
        <tr>
          <td id="L82" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="82"></td>
          <td id="LC82" class="blob-code blob-code-inner js-file-line">            </td>
        </tr>
        <tr>
          <td id="L83" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="83"></td>
          <td id="LC83" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span>(<span class="pl-s1">num</span><span class="pl-c1">==</span><span class="pl-c1">2</span>):</td>
        </tr>
        <tr>
          <td id="L84" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="84"></td>
          <td id="LC84" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-s1">pls</span>[<span class="pl-c1">2</span>]:</td>
        </tr>
        <tr>
          <td id="L85" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="85"></td>
          <td id="LC85" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>] <span class="pl-c1">=</span> <span class="pl-v">Button</span>(<span class="pl-s1">t</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s1">i</span>, <span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"Black"</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">"verdana"</span>,<span class="pl-c1">16</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">command</span><span class="pl-c1">=</span><span class="pl-en">partial</span>(<span class="pl-s1">seats</span>,<span class="pl-s1">i</span>))</td>
        </tr>
        <tr>
          <td id="L86" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="86"></td>
          <td id="LC86" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>].<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">16</span>)</td>
        </tr>
        <tr>
          <td id="L87" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="87"></td>
          <td id="LC87" class="blob-code blob-code-inner js-file-line">            </td>
        </tr>
        <tr>
          <td id="L88" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="88"></td>
          <td id="LC88" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span>(<span class="pl-s1">num</span><span class="pl-c1">==</span><span class="pl-c1">3</span>):</td>
        </tr>
        <tr>
          <td id="L89" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="89"></td>
          <td id="LC89" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-s1">pls</span>[<span class="pl-c1">3</span>]:</td>
        </tr>
        <tr>
          <td id="L90" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="90"></td>
          <td id="LC90" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>] <span class="pl-c1">=</span> <span class="pl-v">Button</span>(<span class="pl-s1">t</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s1">i</span>, <span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"Black"</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">"verdana"</span>,<span class="pl-c1">16</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">command</span><span class="pl-c1">=</span><span class="pl-en">partial</span>(<span class="pl-s1">seats</span>,<span class="pl-s1">i</span>))</td>
        </tr>
        <tr>
          <td id="L91" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="91"></td>
          <td id="LC91" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>].<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">16</span>)</td>
        </tr>
        <tr>
          <td id="L92" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="92"></td>
          <td id="LC92" class="blob-code blob-code-inner js-file-line">            </td>
        </tr>
        <tr>
          <td id="L93" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="93"></td>
          <td id="LC93" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span>(<span class="pl-s1">num</span><span class="pl-c1">==</span><span class="pl-c1">4</span>):</td>
        </tr>
        <tr>
          <td id="L94" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="94"></td>
          <td id="LC94" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-s1">pls</span>[<span class="pl-c1">4</span>]:</td>
        </tr>
        <tr>
          <td id="L95" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="95"></td>
          <td id="LC95" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>] <span class="pl-c1">=</span> <span class="pl-v">Button</span>(<span class="pl-s1">t</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s1">i</span>, <span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"Black"</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">"verdana"</span>,<span class="pl-c1">16</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">command</span><span class="pl-c1">=</span><span class="pl-en">partial</span>(<span class="pl-s1">seats</span>,<span class="pl-s1">i</span>))</td>
        </tr>
        <tr>
          <td id="L96" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="96"></td>
          <td id="LC96" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>].<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">16</span>)</td>
        </tr>
        <tr>
          <td id="L97" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="97"></td>
          <td id="LC97" class="blob-code blob-code-inner js-file-line">            </td>
        </tr>
        <tr>
          <td id="L98" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="98"></td>
          <td id="LC98" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">jurassictimes</span>(<span class="pl-s1">num</span>,<span class="pl-s1">i</span>):</td>
        </tr>
        <tr>
          <td id="L99" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="99"></td>
          <td id="LC99" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">booking</span>[<span class="pl-s">'Theatre Name'</span>]<span class="pl-c1">=</span><span class="pl-s1">i</span></td>
        </tr>
        <tr>
          <td id="L100" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="100"></td>
          <td id="LC100" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">with</span> <span class="pl-en">open</span>(<span class="pl-s">'bookings.json'</span>,<span class="pl-s">'w'</span>) <span class="pl-k">as</span> <span class="pl-s1">file</span>:</td>
        </tr>
        <tr>
          <td id="L101" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="101"></td>
          <td id="LC101" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">json</span>.<span class="pl-en">dump</span>(<span class="pl-s1">booking</span>,<span class="pl-s1">file</span>)</td>
        </tr>
        <tr>
          <td id="L102" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="102"></td>
          <td id="LC102" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">t</span><span class="pl-c1">=</span><span class="pl-v">Tk</span>()</td>
        </tr>
        <tr>
          <td id="L103" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="103"></td>
          <td id="LC103" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">t</span>.<span class="pl-en">geometry</span>(<span class="pl-s">"1000x2000+10+20"</span>)</td>
        </tr>
        <tr>
          <td id="L104" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="104"></td>
          <td id="LC104" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">t</span>.<span class="pl-en">state</span>(<span class="pl-s">"zoomed"</span>)</td>
        </tr>
        <tr>
          <td id="L105" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="105"></td>
          <td id="LC105" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">t</span>[<span class="pl-s">'bg'</span>] <span class="pl-c1">=</span> <span class="pl-s">"deepskyblue"</span></td>
        </tr>
        <tr>
          <td id="L106" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="106"></td>
          <td id="LC106" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">heading</span> <span class="pl-c1">=</span> <span class="pl-v">Label</span>(<span class="pl-s1">t</span>,<span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s">"Timings"</span>,<span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">'verdana'</span>,<span class="pl-c1">25</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"black"</span>,<span class="pl-s1">bg</span><span class="pl-c1">=</span><span class="pl-s">"deepskyblue"</span>)</td>
        </tr>
        <tr>
          <td id="L107" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="107"></td>
          <td id="LC107" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">heading</span>.<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">10</span>)</td>
        </tr>
        <tr>
          <td id="L108" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="108"></td>
          <td id="LC108" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">style1</span> <span class="pl-c1">=</span> <span class="pl-v">Label</span>(<span class="pl-s1">t</span>,<span class="pl-s1">bg</span><span class="pl-c1">=</span><span class="pl-s">"black"</span>,<span class="pl-s1">height</span><span class="pl-c1">=</span><span class="pl-c1">1</span>,<span class="pl-s1">width</span><span class="pl-c1">=</span><span class="pl-c1">500</span>)</td>
        </tr>
        <tr>
          <td id="L109" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="109"></td>
          <td id="LC109" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">style1</span>.<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">10</span>)</td>
        </tr>
        <tr>
          <td id="L110" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="110"></td>
          <td id="LC110" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">button_dict</span><span class="pl-c1">=</span>{}</td>
        </tr>
        <tr>
          <td id="L111" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="111"></td>
          <td id="LC111" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">with</span> <span class="pl-en">open</span>(<span class="pl-s">"jurassic.json"</span>,<span class="pl-s">'r'</span>) <span class="pl-k">as</span> <span class="pl-s1">file</span>:</td>
        </tr>
        <tr>
          <td id="L112" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="112"></td>
          <td id="LC112" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">a</span><span class="pl-c1">=</span><span class="pl-s1">json</span>.<span class="pl-en">load</span>(<span class="pl-s1">file</span>)</td>
        </tr>
        <tr>
          <td id="L113" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="113"></td>
          <td id="LC113" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">pls</span><span class="pl-c1">=</span>[]</td>
        </tr>
        <tr>
          <td id="L114" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="114"></td>
          <td id="LC114" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-s1">a</span>.<span class="pl-en">values</span>():</td>
        </tr>
        <tr>
          <td id="L115" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="115"></td>
          <td id="LC115" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">pls</span>.<span class="pl-en">append</span>(<span class="pl-s1">i</span>)</td>
        </tr>
        <tr>
          <td id="L116" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="116"></td>
          <td id="LC116" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span>(<span class="pl-s1">num</span><span class="pl-c1">==</span><span class="pl-c1">0</span>):</td>
        </tr>
        <tr>
          <td id="L117" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="117"></td>
          <td id="LC117" class="blob-code blob-code-inner js-file-line">       <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-s1">pls</span>[<span class="pl-c1">0</span>]:</td>
        </tr>
        <tr>
          <td id="L118" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="118"></td>
          <td id="LC118" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>] <span class="pl-c1">=</span> <span class="pl-v">Button</span>(<span class="pl-s1">t</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s1">i</span>, <span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"Black"</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">"verdana"</span>,<span class="pl-c1">16</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">command</span><span class="pl-c1">=</span><span class="pl-en">partial</span>(<span class="pl-s1">seats</span>,<span class="pl-s1">i</span>))</td>
        </tr>
        <tr>
          <td id="L119" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="119"></td>
          <td id="LC119" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>].<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">16</span>)</td>
        </tr>
        <tr>
          <td id="L120" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="120"></td>
          <td id="LC120" class="blob-code blob-code-inner js-file-line">    </td>
        </tr>
        <tr>
          <td id="L121" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="121"></td>
          <td id="LC121" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span>(<span class="pl-s1">num</span><span class="pl-c1">==</span><span class="pl-c1">1</span>):</td>
        </tr>
        <tr>
          <td id="L122" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="122"></td>
          <td id="LC122" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-s1">pls</span>[<span class="pl-c1">1</span>]:</td>
        </tr>
        <tr>
          <td id="L123" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="123"></td>
          <td id="LC123" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>] <span class="pl-c1">=</span> <span class="pl-v">Button</span>(<span class="pl-s1">t</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s1">i</span>, <span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"Black"</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">"verdana"</span>,<span class="pl-c1">16</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">command</span><span class="pl-c1">=</span><span class="pl-en">partial</span>(<span class="pl-s1">seats</span>,<span class="pl-s1">i</span>))</td>
        </tr>
        <tr>
          <td id="L124" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="124"></td>
          <td id="LC124" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>].<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">16</span>)</td>
        </tr>
        <tr>
          <td id="L125" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="125"></td>
          <td id="LC125" class="blob-code blob-code-inner js-file-line">            </td>
        </tr>
        <tr>
          <td id="L126" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="126"></td>
          <td id="LC126" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span>(<span class="pl-s1">num</span><span class="pl-c1">==</span><span class="pl-c1">2</span>):</td>
        </tr>
        <tr>
          <td id="L127" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="127"></td>
          <td id="LC127" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-s1">pls</span>[<span class="pl-c1">2</span>]:</td>
        </tr>
        <tr>
          <td id="L128" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="128"></td>
          <td id="LC128" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>] <span class="pl-c1">=</span> <span class="pl-v">Button</span>(<span class="pl-s1">t</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s1">i</span>, <span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"Black"</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">"verdana"</span>,<span class="pl-c1">16</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">command</span><span class="pl-c1">=</span><span class="pl-en">partial</span>(<span class="pl-s1">seats</span>,<span class="pl-s1">i</span>))</td>
        </tr>
        <tr>
          <td id="L129" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="129"></td>
          <td id="LC129" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>].<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">16</span>)</td>
        </tr>
        <tr>
          <td id="L130" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="130"></td>
          <td id="LC130" class="blob-code blob-code-inner js-file-line">
</td>
        </tr>
        <tr>
          <td id="L131" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="131"></td>
          <td id="LC131" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">charlietimes</span>(<span class="pl-s1">num</span>,<span class="pl-s1">i</span>):</td>
        </tr>
        <tr>
          <td id="L132" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="132"></td>
          <td id="LC132" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">booking</span>[<span class="pl-s">'Theatre Name'</span>]<span class="pl-c1">=</span><span class="pl-s1">i</span></td>
        </tr>
        <tr>
          <td id="L133" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="133"></td>
          <td id="LC133" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">with</span> <span class="pl-en">open</span>(<span class="pl-s">'bookings.json'</span>,<span class="pl-s">'w'</span>) <span class="pl-k">as</span> <span class="pl-s1">file</span>:</td>
        </tr>
        <tr>
          <td id="L134" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="134"></td>
          <td id="LC134" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">json</span>.<span class="pl-en">dump</span>(<span class="pl-s1">booking</span>,<span class="pl-s1">file</span>)</td>
        </tr>
        <tr>
          <td id="L135" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="135"></td>
          <td id="LC135" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">t</span><span class="pl-c1">=</span><span class="pl-v">Tk</span>()</td>
        </tr>
        <tr>
          <td id="L136" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="136"></td>
          <td id="LC136" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">t</span>.<span class="pl-en">geometry</span>(<span class="pl-s">"1000x2000+10+20"</span>)</td>
        </tr>
        <tr>
          <td id="L137" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="137"></td>
          <td id="LC137" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">t</span>.<span class="pl-en">state</span>(<span class="pl-s">"zoomed"</span>)</td>
        </tr>
        <tr>
          <td id="L138" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="138"></td>
          <td id="LC138" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">t</span>[<span class="pl-s">'bg'</span>] <span class="pl-c1">=</span> <span class="pl-s">"deepskyblue"</span></td>
        </tr>
        <tr>
          <td id="L139" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="139"></td>
          <td id="LC139" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">heading</span> <span class="pl-c1">=</span> <span class="pl-v">Label</span>(<span class="pl-s1">t</span>,<span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s">"Timings"</span>,<span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">'verdana'</span>,<span class="pl-c1">25</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"black"</span>,<span class="pl-s1">bg</span><span class="pl-c1">=</span><span class="pl-s">"deepskyblue"</span>)</td>
        </tr>
        <tr>
          <td id="L140" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="140"></td>
          <td id="LC140" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">heading</span>.<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">10</span>)</td>
        </tr>
        <tr>
          <td id="L141" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="141"></td>
          <td id="LC141" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">style1</span> <span class="pl-c1">=</span> <span class="pl-v">Label</span>(<span class="pl-s1">t</span>,<span class="pl-s1">bg</span><span class="pl-c1">=</span><span class="pl-s">"black"</span>,<span class="pl-s1">height</span><span class="pl-c1">=</span><span class="pl-c1">1</span>,<span class="pl-s1">width</span><span class="pl-c1">=</span><span class="pl-c1">500</span>)</td>
        </tr>
        <tr>
          <td id="L142" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="142"></td>
          <td id="LC142" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">style1</span>.<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">10</span>)</td>
        </tr>
        <tr>
          <td id="L143" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="143"></td>
          <td id="LC143" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">button_dict</span><span class="pl-c1">=</span>{}</td>
        </tr>
        <tr>
          <td id="L144" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="144"></td>
          <td id="LC144" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">with</span> <span class="pl-en">open</span>(<span class="pl-s">"charlie.json"</span>,<span class="pl-s">'r'</span>) <span class="pl-k">as</span> <span class="pl-s1">file</span>:</td>
        </tr>
        <tr>
          <td id="L145" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="145"></td>
          <td id="LC145" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">a</span><span class="pl-c1">=</span><span class="pl-s1">json</span>.<span class="pl-en">load</span>(<span class="pl-s1">file</span>)</td>
        </tr>
        <tr>
          <td id="L146" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="146"></td>
          <td id="LC146" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">pls</span><span class="pl-c1">=</span>[]</td>
        </tr>
        <tr>
          <td id="L147" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="147"></td>
          <td id="LC147" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-s1">a</span>.<span class="pl-en">values</span>():</td>
        </tr>
        <tr>
          <td id="L148" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="148"></td>
          <td id="LC148" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">pls</span>.<span class="pl-en">append</span>(<span class="pl-s1">i</span>)</td>
        </tr>
        <tr>
          <td id="L149" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="149"></td>
          <td id="LC149" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span>(<span class="pl-s1">num</span><span class="pl-c1">==</span><span class="pl-c1">0</span>):</td>
        </tr>
        <tr>
          <td id="L150" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="150"></td>
          <td id="LC150" class="blob-code blob-code-inner js-file-line">       <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-s1">pls</span>[<span class="pl-c1">0</span>]:</td>
        </tr>
        <tr>
          <td id="L151" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="151"></td>
          <td id="LC151" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>] <span class="pl-c1">=</span> <span class="pl-v">Button</span>(<span class="pl-s1">t</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s1">i</span>, <span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"Black"</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">"verdana"</span>,<span class="pl-c1">16</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">command</span><span class="pl-c1">=</span><span class="pl-en">partial</span>(<span class="pl-s1">seats</span>,<span class="pl-s1">i</span>))</td>
        </tr>
        <tr>
          <td id="L152" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="152"></td>
          <td id="LC152" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>].<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">16</span>)</td>
        </tr>
        <tr>
          <td id="L153" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="153"></td>
          <td id="LC153" class="blob-code blob-code-inner js-file-line">    </td>
        </tr>
        <tr>
          <td id="L154" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="154"></td>
          <td id="LC154" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span>(<span class="pl-s1">num</span><span class="pl-c1">==</span><span class="pl-c1">1</span>):</td>
        </tr>
        <tr>
          <td id="L155" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="155"></td>
          <td id="LC155" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-s1">pls</span>[<span class="pl-c1">1</span>]:</td>
        </tr>
        <tr>
          <td id="L156" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="156"></td>
          <td id="LC156" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>] <span class="pl-c1">=</span> <span class="pl-v">Button</span>(<span class="pl-s1">t</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s1">i</span>, <span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"Black"</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">"verdana"</span>,<span class="pl-c1">16</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">command</span><span class="pl-c1">=</span><span class="pl-en">partial</span>(<span class="pl-s1">seats</span>,<span class="pl-s1">i</span>))</td>
        </tr>
        <tr>
          <td id="L157" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="157"></td>
          <td id="LC157" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>].<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">16</span>)</td>
        </tr>
        <tr>
          <td id="L158" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="158"></td>
          <td id="LC158" class="blob-code blob-code-inner js-file-line">            </td>
        </tr>
        <tr>
          <td id="L159" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="159"></td>
          <td id="LC159" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span>(<span class="pl-s1">num</span><span class="pl-c1">==</span><span class="pl-c1">2</span>):</td>
        </tr>
        <tr>
          <td id="L160" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="160"></td>
          <td id="LC160" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-s1">pls</span>[<span class="pl-c1">2</span>]:</td>
        </tr>
        <tr>
          <td id="L161" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="161"></td>
          <td id="LC161" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>] <span class="pl-c1">=</span> <span class="pl-v">Button</span>(<span class="pl-s1">t</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s1">i</span>, <span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"Black"</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">"verdana"</span>,<span class="pl-c1">16</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">command</span><span class="pl-c1">=</span><span class="pl-en">partial</span>(<span class="pl-s1">seats</span>,<span class="pl-s1">i</span>))</td>
        </tr>
        <tr>
          <td id="L162" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="162"></td>
          <td id="LC162" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>].<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">16</span>)</td>
        </tr>
        <tr>
          <td id="L163" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="163"></td>
          <td id="LC163" class="blob-code blob-code-inner js-file-line">            </td>
        </tr>
        <tr>
          <td id="L164" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="164"></td>
          <td id="LC164" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">dontimes</span>(<span class="pl-s1">num</span>,<span class="pl-s1">i</span>):</td>
        </tr>
        <tr>
          <td id="L165" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="165"></td>
          <td id="LC165" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">booking</span>[<span class="pl-s">'Theatre Name'</span>]<span class="pl-c1">=</span><span class="pl-s1">i</span></td>
        </tr>
        <tr>
          <td id="L166" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="166"></td>
          <td id="LC166" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">with</span> <span class="pl-en">open</span>(<span class="pl-s">'bookings.json'</span>,<span class="pl-s">'w'</span>) <span class="pl-k">as</span> <span class="pl-s1">file</span>:</td>
        </tr>
        <tr>
          <td id="L167" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="167"></td>
          <td id="LC167" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">json</span>.<span class="pl-en">dump</span>(<span class="pl-s1">booking</span>,<span class="pl-s1">file</span>)</td>
        </tr>
        <tr>
          <td id="L168" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="168"></td>
          <td id="LC168" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">t</span><span class="pl-c1">=</span><span class="pl-v">Tk</span>()</td>
        </tr>
        <tr>
          <td id="L169" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="169"></td>
          <td id="LC169" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">t</span>.<span class="pl-en">geometry</span>(<span class="pl-s">"1000x2000+10+20"</span>)</td>
        </tr>
        <tr>
          <td id="L170" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="170"></td>
          <td id="LC170" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">t</span>.<span class="pl-en">state</span>(<span class="pl-s">"zoomed"</span>)</td>
        </tr>
        <tr>
          <td id="L171" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="171"></td>
          <td id="LC171" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">t</span>[<span class="pl-s">'bg'</span>] <span class="pl-c1">=</span> <span class="pl-s">"deepskyblue"</span></td>
        </tr>
        <tr>
          <td id="L172" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="172"></td>
          <td id="LC172" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">heading</span> <span class="pl-c1">=</span> <span class="pl-v">Label</span>(<span class="pl-s1">t</span>,<span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s">"Timings"</span>,<span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">'verdana'</span>,<span class="pl-c1">25</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"black"</span>,<span class="pl-s1">bg</span><span class="pl-c1">=</span><span class="pl-s">"deepskyblue"</span>)</td>
        </tr>
        <tr>
          <td id="L173" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="173"></td>
          <td id="LC173" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">heading</span>.<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">10</span>)</td>
        </tr>
        <tr>
          <td id="L174" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="174"></td>
          <td id="LC174" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">style1</span> <span class="pl-c1">=</span> <span class="pl-v">Label</span>(<span class="pl-s1">t</span>,<span class="pl-s1">bg</span><span class="pl-c1">=</span><span class="pl-s">"black"</span>,<span class="pl-s1">height</span><span class="pl-c1">=</span><span class="pl-c1">1</span>,<span class="pl-s1">width</span><span class="pl-c1">=</span><span class="pl-c1">500</span>)</td>
        </tr>
        <tr>
          <td id="L175" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="175"></td>
          <td id="LC175" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">style1</span>.<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">10</span>)</td>
        </tr>
        <tr>
          <td id="L176" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="176"></td>
          <td id="LC176" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">button_dict</span><span class="pl-c1">=</span>{}</td>
        </tr>
        <tr>
          <td id="L177" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="177"></td>
          <td id="LC177" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">with</span> <span class="pl-en">open</span>(<span class="pl-s">"don.json"</span>,<span class="pl-s">'r'</span>) <span class="pl-k">as</span> <span class="pl-s1">file</span>:</td>
        </tr>
        <tr>
          <td id="L178" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="178"></td>
          <td id="LC178" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">a</span><span class="pl-c1">=</span><span class="pl-s1">json</span>.<span class="pl-en">load</span>(<span class="pl-s1">file</span>)</td>
        </tr>
        <tr>
          <td id="L179" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="179"></td>
          <td id="LC179" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">pls</span><span class="pl-c1">=</span>[]</td>
        </tr>
        <tr>
          <td id="L180" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="180"></td>
          <td id="LC180" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-s1">a</span>.<span class="pl-en">values</span>():</td>
        </tr>
        <tr>
          <td id="L181" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="181"></td>
          <td id="LC181" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">pls</span>.<span class="pl-en">append</span>(<span class="pl-s1">i</span>)</td>
        </tr>
        <tr>
          <td id="L182" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="182"></td>
          <td id="LC182" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span>(<span class="pl-s1">num</span><span class="pl-c1">==</span><span class="pl-c1">0</span>):</td>
        </tr>
        <tr>
          <td id="L183" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="183"></td>
          <td id="LC183" class="blob-code blob-code-inner js-file-line">       <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-s1">pls</span>[<span class="pl-c1">0</span>]:</td>
        </tr>
        <tr>
          <td id="L184" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="184"></td>
          <td id="LC184" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>] <span class="pl-c1">=</span> <span class="pl-v">Button</span>(<span class="pl-s1">t</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s1">i</span>, <span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"Black"</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">"verdana"</span>,<span class="pl-c1">16</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">command</span><span class="pl-c1">=</span><span class="pl-en">partial</span>(<span class="pl-s1">seats</span>,<span class="pl-s1">i</span>))</td>
        </tr>
        <tr>
          <td id="L185" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="185"></td>
          <td id="LC185" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>].<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">16</span>)</td>
        </tr>
        <tr>
          <td id="L186" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="186"></td>
          <td id="LC186" class="blob-code blob-code-inner js-file-line">    </td>
        </tr>
        <tr>
          <td id="L187" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="187"></td>
          <td id="LC187" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span>(<span class="pl-s1">num</span><span class="pl-c1">==</span><span class="pl-c1">1</span>):</td>
        </tr>
        <tr>
          <td id="L188" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="188"></td>
          <td id="LC188" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-s1">pls</span>[<span class="pl-c1">1</span>]:</td>
        </tr>
        <tr>
          <td id="L189" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="189"></td>
          <td id="LC189" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>] <span class="pl-c1">=</span> <span class="pl-v">Button</span>(<span class="pl-s1">t</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s1">i</span>, <span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"Black"</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">"verdana"</span>,<span class="pl-c1">16</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">command</span><span class="pl-c1">=</span><span class="pl-en">partial</span>(<span class="pl-s1">seats</span>,<span class="pl-s1">i</span>))</td>
        </tr>
        <tr>
          <td id="L190" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="190"></td>
          <td id="LC190" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>].<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">16</span>)</td>
        </tr>
        <tr>
          <td id="L191" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="191"></td>
          <td id="LC191" class="blob-code blob-code-inner js-file-line">            </td>
        </tr>
        <tr>
          <td id="L192" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="192"></td>
          <td id="LC192" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span>(<span class="pl-s1">num</span><span class="pl-c1">==</span><span class="pl-c1">2</span>):</td>
        </tr>
        <tr>
          <td id="L193" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="193"></td>
          <td id="LC193" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-s1">pls</span>[<span class="pl-c1">2</span>]:</td>
        </tr>
        <tr>
          <td id="L194" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="194"></td>
          <td id="LC194" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>] <span class="pl-c1">=</span> <span class="pl-v">Button</span>(<span class="pl-s1">t</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s1">i</span>, <span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"Black"</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">"verdana"</span>,<span class="pl-c1">16</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">command</span><span class="pl-c1">=</span><span class="pl-en">partial</span>(<span class="pl-s1">seats</span>,<span class="pl-s1">i</span>))</td>
        </tr>
        <tr>
          <td id="L195" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="195"></td>
          <td id="LC195" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>].<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">16</span>)</td>
        </tr>
        <tr>
          <td id="L196" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="196"></td>
          <td id="LC196" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span>(<span class="pl-s1">num</span><span class="pl-c1">==</span><span class="pl-c1">3</span>):</td>
        </tr>
        <tr>
          <td id="L197" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="197"></td>
          <td id="LC197" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-s1">pls</span>[<span class="pl-c1">3</span>]:</td>
        </tr>
        <tr>
          <td id="L198" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="198"></td>
          <td id="LC198" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>] <span class="pl-c1">=</span> <span class="pl-v">Button</span>(<span class="pl-s1">t</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s1">i</span>, <span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"Black"</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">"verdana"</span>,<span class="pl-c1">16</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">command</span><span class="pl-c1">=</span><span class="pl-en">partial</span>(<span class="pl-s1">seats</span>,<span class="pl-s1">i</span>))</td>
        </tr>
        <tr>
          <td id="L199" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="199"></td>
          <td id="LC199" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>].<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">16</span>)</td>
        </tr>
        <tr>
          <td id="L200" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="200"></td>
          <td id="LC200" class="blob-code blob-code-inner js-file-line">            </td>
        </tr>
        <tr>
          <td id="L201" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="201"></td>
          <td id="LC201" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">adadetimes</span>(<span class="pl-s1">num</span>,<span class="pl-s1">i</span>):</td>
        </tr>
        <tr>
          <td id="L202" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="202"></td>
          <td id="LC202" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">booking</span>[<span class="pl-s">'Theatre Name'</span>]<span class="pl-c1">=</span><span class="pl-s1">i</span></td>
        </tr>
        <tr>
          <td id="L203" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="203"></td>
          <td id="LC203" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">with</span> <span class="pl-en">open</span>(<span class="pl-s">'bookings.json'</span>,<span class="pl-s">'w'</span>) <span class="pl-k">as</span> <span class="pl-s1">file</span>:</td>
        </tr>
        <tr>
          <td id="L204" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="204"></td>
          <td id="LC204" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">json</span>.<span class="pl-en">dump</span>(<span class="pl-s1">booking</span>,<span class="pl-s1">file</span>)</td>
        </tr>
        <tr>
          <td id="L205" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="205"></td>
          <td id="LC205" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">t</span><span class="pl-c1">=</span><span class="pl-v">Tk</span>()</td>
        </tr>
        <tr>
          <td id="L206" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="206"></td>
          <td id="LC206" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">t</span>.<span class="pl-en">geometry</span>(<span class="pl-s">"1000x2000+10+20"</span>)</td>
        </tr>
        <tr>
          <td id="L207" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="207"></td>
          <td id="LC207" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">t</span>.<span class="pl-en">state</span>(<span class="pl-s">"zoomed"</span>)</td>
        </tr>
        <tr>
          <td id="L208" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="208"></td>
          <td id="LC208" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">t</span>[<span class="pl-s">'bg'</span>] <span class="pl-c1">=</span> <span class="pl-s">"deepskyblue"</span></td>
        </tr>
        <tr>
          <td id="L209" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="209"></td>
          <td id="LC209" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">heading</span> <span class="pl-c1">=</span> <span class="pl-v">Label</span>(<span class="pl-s1">t</span>,<span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s">"Timings"</span>,<span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">'verdana'</span>,<span class="pl-c1">25</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"black"</span>,<span class="pl-s1">bg</span><span class="pl-c1">=</span><span class="pl-s">"deepskyblue"</span>)</td>
        </tr>
        <tr>
          <td id="L210" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="210"></td>
          <td id="LC210" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">heading</span>.<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">10</span>)</td>
        </tr>
        <tr>
          <td id="L211" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="211"></td>
          <td id="LC211" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">style1</span> <span class="pl-c1">=</span> <span class="pl-v">Label</span>(<span class="pl-s1">t</span>,<span class="pl-s1">bg</span><span class="pl-c1">=</span><span class="pl-s">"black"</span>,<span class="pl-s1">height</span><span class="pl-c1">=</span><span class="pl-c1">1</span>,<span class="pl-s1">width</span><span class="pl-c1">=</span><span class="pl-c1">500</span>)</td>
        </tr>
        <tr>
          <td id="L212" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="212"></td>
          <td id="LC212" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">style1</span>.<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">10</span>)</td>
        </tr>
        <tr>
          <td id="L213" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="213"></td>
          <td id="LC213" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">button_dict</span><span class="pl-c1">=</span>{}</td>
        </tr>
        <tr>
          <td id="L214" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="214"></td>
          <td id="LC214" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">with</span> <span class="pl-en">open</span>(<span class="pl-s">"adade.json"</span>,<span class="pl-s">'r'</span>) <span class="pl-k">as</span> <span class="pl-s1">file</span>:</td>
        </tr>
        <tr>
          <td id="L215" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="215"></td>
          <td id="LC215" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">a</span><span class="pl-c1">=</span><span class="pl-s1">json</span>.<span class="pl-en">load</span>(<span class="pl-s1">file</span>)</td>
        </tr>
        <tr>
          <td id="L216" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="216"></td>
          <td id="LC216" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">pls</span><span class="pl-c1">=</span>[]</td>
        </tr>
        <tr>
          <td id="L217" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="217"></td>
          <td id="LC217" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-s1">a</span>.<span class="pl-en">values</span>():</td>
        </tr>
        <tr>
          <td id="L218" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="218"></td>
          <td id="LC218" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">pls</span>.<span class="pl-en">append</span>(<span class="pl-s1">i</span>)</td>
        </tr>
        <tr>
          <td id="L219" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="219"></td>
          <td id="LC219" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span>(<span class="pl-s1">num</span><span class="pl-c1">==</span><span class="pl-c1">0</span>):</td>
        </tr>
        <tr>
          <td id="L220" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="220"></td>
          <td id="LC220" class="blob-code blob-code-inner js-file-line">       <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-s1">pls</span>[<span class="pl-c1">0</span>]:</td>
        </tr>
        <tr>
          <td id="L221" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="221"></td>
          <td id="LC221" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>] <span class="pl-c1">=</span> <span class="pl-v">Button</span>(<span class="pl-s1">t</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s1">i</span>, <span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"Black"</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">"verdana"</span>,<span class="pl-c1">16</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">command</span><span class="pl-c1">=</span><span class="pl-en">partial</span>(<span class="pl-s1">seats</span>,<span class="pl-s1">i</span>))</td>
        </tr>
        <tr>
          <td id="L222" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="222"></td>
          <td id="LC222" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>].<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">16</span>)</td>
        </tr>
        <tr>
          <td id="L223" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="223"></td>
          <td id="LC223" class="blob-code blob-code-inner js-file-line">    </td>
        </tr>
        <tr>
          <td id="L224" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="224"></td>
          <td id="LC224" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span>(<span class="pl-s1">num</span><span class="pl-c1">==</span><span class="pl-c1">1</span>):</td>
        </tr>
        <tr>
          <td id="L225" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="225"></td>
          <td id="LC225" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-s1">pls</span>[<span class="pl-c1">1</span>]:</td>
        </tr>
        <tr>
          <td id="L226" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="226"></td>
          <td id="LC226" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>] <span class="pl-c1">=</span> <span class="pl-v">Button</span>(<span class="pl-s1">t</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s1">i</span>, <span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"Black"</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">"verdana"</span>,<span class="pl-c1">16</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">command</span><span class="pl-c1">=</span><span class="pl-en">partial</span>(<span class="pl-s1">seats</span>,<span class="pl-s1">i</span>))</td>
        </tr>
        <tr>
          <td id="L227" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="227"></td>
          <td id="LC227" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>].<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">16</span>)</td>
        </tr>
        <tr>
          <td id="L228" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="228"></td>
          <td id="LC228" class="blob-code blob-code-inner js-file-line">            </td>
        </tr>
        <tr>
          <td id="L229" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="229"></td>
          <td id="LC229" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span>(<span class="pl-s1">num</span><span class="pl-c1">==</span><span class="pl-c1">2</span>):</td>
        </tr>
        <tr>
          <td id="L230" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="230"></td>
          <td id="LC230" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-s1">pls</span>[<span class="pl-c1">2</span>]:</td>
        </tr>
        <tr>
          <td id="L231" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="231"></td>
          <td id="LC231" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>] <span class="pl-c1">=</span> <span class="pl-v">Button</span>(<span class="pl-s1">t</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s1">i</span>, <span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"Black"</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">"verdana"</span>,<span class="pl-c1">16</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">command</span><span class="pl-c1">=</span><span class="pl-en">partial</span>(<span class="pl-s1">seats</span>,<span class="pl-s1">i</span>))</td>
        </tr>
        <tr>
          <td id="L232" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="232"></td>
          <td id="LC232" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>].<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">16</span>)</td>
        </tr>
        <tr>
          <td id="L233" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="233"></td>
          <td id="LC233" class="blob-code blob-code-inner js-file-line">            </td>
        </tr>
        <tr>
          <td id="L234" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="234"></td>
          <td id="LC234" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">ejurassictimes</span>(<span class="pl-s1">num</span>,<span class="pl-s1">i</span>):</td>
        </tr>
        <tr>
          <td id="L235" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="235"></td>
          <td id="LC235" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">booking</span>[<span class="pl-s">'Theatre Name'</span>]<span class="pl-c1">=</span><span class="pl-s1">i</span></td>
        </tr>
        <tr>
          <td id="L236" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="236"></td>
          <td id="LC236" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">with</span> <span class="pl-en">open</span>(<span class="pl-s">'bookings.json'</span>,<span class="pl-s">'w'</span>) <span class="pl-k">as</span> <span class="pl-s1">file</span>:</td>
        </tr>
        <tr>
          <td id="L237" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="237"></td>
          <td id="LC237" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">json</span>.<span class="pl-en">dump</span>(<span class="pl-s1">booking</span>,<span class="pl-s1">file</span>)</td>
        </tr>
        <tr>
          <td id="L238" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="238"></td>
          <td id="LC238" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">t</span><span class="pl-c1">=</span><span class="pl-v">Tk</span>()</td>
        </tr>
        <tr>
          <td id="L239" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="239"></td>
          <td id="LC239" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">t</span>.<span class="pl-en">geometry</span>(<span class="pl-s">"1000x2000+10+20"</span>)</td>
        </tr>
        <tr>
          <td id="L240" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="240"></td>
          <td id="LC240" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">t</span>.<span class="pl-en">state</span>(<span class="pl-s">"zoomed"</span>)</td>
        </tr>
        <tr>
          <td id="L241" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="241"></td>
          <td id="LC241" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">t</span>[<span class="pl-s">'bg'</span>] <span class="pl-c1">=</span> <span class="pl-s">"deepskyblue"</span></td>
        </tr>
        <tr>
          <td id="L242" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="242"></td>
          <td id="LC242" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">heading</span> <span class="pl-c1">=</span> <span class="pl-v">Label</span>(<span class="pl-s1">t</span>,<span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s">"Timings"</span>,<span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">'verdana'</span>,<span class="pl-c1">25</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"black"</span>,<span class="pl-s1">bg</span><span class="pl-c1">=</span><span class="pl-s">"deepskyblue"</span>)</td>
        </tr>
        <tr>
          <td id="L243" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="243"></td>
          <td id="LC243" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">heading</span>.<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">10</span>)</td>
        </tr>
        <tr>
          <td id="L244" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="244"></td>
          <td id="LC244" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">style1</span> <span class="pl-c1">=</span> <span class="pl-v">Label</span>(<span class="pl-s1">t</span>,<span class="pl-s1">bg</span><span class="pl-c1">=</span><span class="pl-s">"black"</span>,<span class="pl-s1">height</span><span class="pl-c1">=</span><span class="pl-c1">1</span>,<span class="pl-s1">width</span><span class="pl-c1">=</span><span class="pl-c1">500</span>)</td>
        </tr>
        <tr>
          <td id="L245" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="245"></td>
          <td id="LC245" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">style1</span>.<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">10</span>)</td>
        </tr>
        <tr>
          <td id="L246" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="246"></td>
          <td id="LC246" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">button_dict</span><span class="pl-c1">=</span>{}</td>
        </tr>
        <tr>
          <td id="L247" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="247"></td>
          <td id="LC247" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">with</span> <span class="pl-en">open</span>(<span class="pl-s">"ejurassic.json"</span>,<span class="pl-s">'r'</span>) <span class="pl-k">as</span> <span class="pl-s1">file</span>:</td>
        </tr>
        <tr>
          <td id="L248" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="248"></td>
          <td id="LC248" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">a</span><span class="pl-c1">=</span><span class="pl-s1">json</span>.<span class="pl-en">load</span>(<span class="pl-s1">file</span>)</td>
        </tr>
        <tr>
          <td id="L249" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="249"></td>
          <td id="LC249" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">pls</span><span class="pl-c1">=</span>[]</td>
        </tr>
        <tr>
          <td id="L250" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="250"></td>
          <td id="LC250" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-s1">a</span>.<span class="pl-en">values</span>():</td>
        </tr>
        <tr>
          <td id="L251" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="251"></td>
          <td id="LC251" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">pls</span>.<span class="pl-en">append</span>(<span class="pl-s1">i</span>)</td>
        </tr>
        <tr>
          <td id="L252" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="252"></td>
          <td id="LC252" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span>(<span class="pl-s1">num</span><span class="pl-c1">==</span><span class="pl-c1">0</span>):</td>
        </tr>
        <tr>
          <td id="L253" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="253"></td>
          <td id="LC253" class="blob-code blob-code-inner js-file-line">       <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-s1">pls</span>[<span class="pl-c1">0</span>]:</td>
        </tr>
        <tr>
          <td id="L254" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="254"></td>
          <td id="LC254" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>] <span class="pl-c1">=</span> <span class="pl-v">Button</span>(<span class="pl-s1">t</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s1">i</span>, <span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"Black"</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">"verdana"</span>,<span class="pl-c1">16</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">command</span><span class="pl-c1">=</span><span class="pl-en">partial</span>(<span class="pl-s1">seats</span>,<span class="pl-s1">i</span>))</td>
        </tr>
        <tr>
          <td id="L255" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="255"></td>
          <td id="LC255" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>].<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">16</span>)</td>
        </tr>
        <tr>
          <td id="L256" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="256"></td>
          <td id="LC256" class="blob-code blob-code-inner js-file-line">    </td>
        </tr>
        <tr>
          <td id="L257" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="257"></td>
          <td id="LC257" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span>(<span class="pl-s1">num</span><span class="pl-c1">==</span><span class="pl-c1">1</span>):</td>
        </tr>
        <tr>
          <td id="L258" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="258"></td>
          <td id="LC258" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-s1">pls</span>[<span class="pl-c1">1</span>]:</td>
        </tr>
        <tr>
          <td id="L259" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="259"></td>
          <td id="LC259" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>] <span class="pl-c1">=</span> <span class="pl-v">Button</span>(<span class="pl-s1">t</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s1">i</span>, <span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"Black"</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">"verdana"</span>,<span class="pl-c1">16</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">command</span><span class="pl-c1">=</span><span class="pl-en">partial</span>(<span class="pl-s1">seats</span>,<span class="pl-s1">i</span>))</td>
        </tr>
        <tr>
          <td id="L260" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="260"></td>
          <td id="LC260" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>].<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">16</span>)</td>
        </tr>
        <tr>
          <td id="L261" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="261"></td>
          <td id="LC261" class="blob-code blob-code-inner js-file-line">            </td>
        </tr>
        <tr>
          <td id="L262" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="262"></td>
          <td id="LC262" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span>(<span class="pl-s1">num</span><span class="pl-c1">==</span><span class="pl-c1">2</span>):</td>
        </tr>
        <tr>
          <td id="L263" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="263"></td>
          <td id="LC263" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-s1">pls</span>[<span class="pl-c1">2</span>]:</td>
        </tr>
        <tr>
          <td id="L264" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="264"></td>
          <td id="LC264" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>] <span class="pl-c1">=</span> <span class="pl-v">Button</span>(<span class="pl-s1">t</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s1">i</span>, <span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"Black"</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">"verdana"</span>,<span class="pl-c1">16</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">command</span><span class="pl-c1">=</span><span class="pl-en">partial</span>(<span class="pl-s1">seats</span>,<span class="pl-s1">i</span>))</td>
        </tr>
        <tr>
          <td id="L265" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="265"></td>
          <td id="LC265" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>].<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">16</span>)</td>
        </tr>
        <tr>
          <td id="L266" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="266"></td>
          <td id="LC266" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span>(<span class="pl-s1">num</span><span class="pl-c1">==</span><span class="pl-c1">3</span>):</td>
        </tr>
        <tr>
          <td id="L267" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="267"></td>
          <td id="LC267" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-s1">pls</span>[<span class="pl-c1">3</span>]:</td>
        </tr>
        <tr>
          <td id="L268" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="268"></td>
          <td id="LC268" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>] <span class="pl-c1">=</span> <span class="pl-v">Button</span>(<span class="pl-s1">t</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s1">i</span>, <span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"Black"</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">"verdana"</span>,<span class="pl-c1">16</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">command</span><span class="pl-c1">=</span><span class="pl-en">partial</span>(<span class="pl-s1">seats</span>,<span class="pl-s1">i</span>))</td>
        </tr>
        <tr>
          <td id="L269" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="269"></td>
          <td id="LC269" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>].<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">16</span>)</td>
        </tr>
        <tr>
          <td id="L270" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="270"></td>
          <td id="LC270" class="blob-code blob-code-inner js-file-line">            </td>
        </tr>
        <tr>
          <td id="L271" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="271"></td>
          <td id="LC271" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">topguntimes</span>(<span class="pl-s1">num</span>,<span class="pl-s1">i</span>):</td>
        </tr>
        <tr>
          <td id="L272" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="272"></td>
          <td id="LC272" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">booking</span>[<span class="pl-s">'Theatre Name'</span>]<span class="pl-c1">=</span><span class="pl-s1">i</span></td>
        </tr>
        <tr>
          <td id="L273" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="273"></td>
          <td id="LC273" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">with</span> <span class="pl-en">open</span>(<span class="pl-s">'bookings.json'</span>,<span class="pl-s">'w'</span>) <span class="pl-k">as</span> <span class="pl-s1">file</span>:</td>
        </tr>
        <tr>
          <td id="L274" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="274"></td>
          <td id="LC274" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">json</span>.<span class="pl-en">dump</span>(<span class="pl-s1">booking</span>,<span class="pl-s1">file</span>)</td>
        </tr>
        <tr>
          <td id="L275" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="275"></td>
          <td id="LC275" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">t</span><span class="pl-c1">=</span><span class="pl-v">Tk</span>()</td>
        </tr>
        <tr>
          <td id="L276" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="276"></td>
          <td id="LC276" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">t</span>.<span class="pl-en">geometry</span>(<span class="pl-s">"1000x2000+10+20"</span>)</td>
        </tr>
        <tr>
          <td id="L277" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="277"></td>
          <td id="LC277" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">t</span>.<span class="pl-en">state</span>(<span class="pl-s">"zoomed"</span>)</td>
        </tr>
        <tr>
          <td id="L278" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="278"></td>
          <td id="LC278" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">t</span>[<span class="pl-s">'bg'</span>] <span class="pl-c1">=</span> <span class="pl-s">"deepskyblue"</span></td>
        </tr>
        <tr>
          <td id="L279" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="279"></td>
          <td id="LC279" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">heading</span> <span class="pl-c1">=</span> <span class="pl-v">Label</span>(<span class="pl-s1">t</span>,<span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s">"Timings"</span>,<span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">'verdana'</span>,<span class="pl-c1">25</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"black"</span>,<span class="pl-s1">bg</span><span class="pl-c1">=</span><span class="pl-s">"deepskyblue"</span>)</td>
        </tr>
        <tr>
          <td id="L280" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="280"></td>
          <td id="LC280" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">heading</span>.<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">10</span>)</td>
        </tr>
        <tr>
          <td id="L281" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="281"></td>
          <td id="LC281" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">style1</span> <span class="pl-c1">=</span> <span class="pl-v">Label</span>(<span class="pl-s1">t</span>,<span class="pl-s1">bg</span><span class="pl-c1">=</span><span class="pl-s">"black"</span>,<span class="pl-s1">height</span><span class="pl-c1">=</span><span class="pl-c1">1</span>,<span class="pl-s1">width</span><span class="pl-c1">=</span><span class="pl-c1">500</span>)</td>
        </tr>
        <tr>
          <td id="L282" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="282"></td>
          <td id="LC282" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">style1</span>.<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">10</span>)</td>
        </tr>
        <tr>
          <td id="L283" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="283"></td>
          <td id="LC283" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">button_dict</span><span class="pl-c1">=</span>{}</td>
        </tr>
        <tr>
          <td id="L284" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="284"></td>
          <td id="LC284" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">with</span> <span class="pl-en">open</span>(<span class="pl-s">"topgun.json"</span>,<span class="pl-s">'r'</span>) <span class="pl-k">as</span> <span class="pl-s1">file</span>:</td>
        </tr>
        <tr>
          <td id="L285" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="285"></td>
          <td id="LC285" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">a</span><span class="pl-c1">=</span><span class="pl-s1">json</span>.<span class="pl-en">load</span>(<span class="pl-s1">file</span>)</td>
        </tr>
        <tr>
          <td id="L286" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="286"></td>
          <td id="LC286" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">pls</span><span class="pl-c1">=</span>[]</td>
        </tr>
        <tr>
          <td id="L287" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="287"></td>
          <td id="LC287" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-s1">a</span>.<span class="pl-en">values</span>():</td>
        </tr>
        <tr>
          <td id="L288" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="288"></td>
          <td id="LC288" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">pls</span>.<span class="pl-en">append</span>(<span class="pl-s1">i</span>)</td>
        </tr>
        <tr>
          <td id="L289" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="289"></td>
          <td id="LC289" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span>(<span class="pl-s1">num</span><span class="pl-c1">==</span><span class="pl-c1">0</span>):</td>
        </tr>
        <tr>
          <td id="L290" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="290"></td>
          <td id="LC290" class="blob-code blob-code-inner js-file-line">       <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-s1">pls</span>[<span class="pl-c1">0</span>]:</td>
        </tr>
        <tr>
          <td id="L291" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="291"></td>
          <td id="LC291" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>] <span class="pl-c1">=</span> <span class="pl-v">Button</span>(<span class="pl-s1">t</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s1">i</span>, <span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"Black"</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">"verdana"</span>,<span class="pl-c1">16</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">command</span><span class="pl-c1">=</span><span class="pl-en">partial</span>(<span class="pl-s1">seats</span>,<span class="pl-s1">i</span>))</td>
        </tr>
        <tr>
          <td id="L292" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="292"></td>
          <td id="LC292" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>].<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">16</span>)</td>
        </tr>
        <tr>
          <td id="L293" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="293"></td>
          <td id="LC293" class="blob-code blob-code-inner js-file-line">    </td>
        </tr>
        <tr>
          <td id="L294" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="294"></td>
          <td id="LC294" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span>(<span class="pl-s1">num</span><span class="pl-c1">==</span><span class="pl-c1">1</span>):</td>
        </tr>
        <tr>
          <td id="L295" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="295"></td>
          <td id="LC295" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-s1">pls</span>[<span class="pl-c1">1</span>]:</td>
        </tr>
        <tr>
          <td id="L296" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="296"></td>
          <td id="LC296" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>] <span class="pl-c1">=</span> <span class="pl-v">Button</span>(<span class="pl-s1">t</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s1">i</span>, <span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"Black"</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">"verdana"</span>,<span class="pl-c1">16</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">command</span><span class="pl-c1">=</span><span class="pl-en">partial</span>(<span class="pl-s1">seats</span>,<span class="pl-s1">i</span>))</td>
        </tr>
        <tr>
          <td id="L297" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="297"></td>
          <td id="LC297" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>].<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">16</span>)</td>
        </tr>
        <tr>
          <td id="L298" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="298"></td>
          <td id="LC298" class="blob-code blob-code-inner js-file-line">            </td>
        </tr>
        <tr>
          <td id="L299" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="299"></td>
          <td id="LC299" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span>(<span class="pl-s1">num</span><span class="pl-c1">==</span><span class="pl-c1">2</span>):</td>
        </tr>
        <tr>
          <td id="L300" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="300"></td>
          <td id="LC300" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-s1">pls</span>[<span class="pl-c1">2</span>]:</td>
        </tr>
        <tr>
          <td id="L301" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="301"></td>
          <td id="LC301" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>] <span class="pl-c1">=</span> <span class="pl-v">Button</span>(<span class="pl-s1">t</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s1">i</span>, <span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"Black"</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">"verdana"</span>,<span class="pl-c1">16</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">command</span><span class="pl-c1">=</span><span class="pl-en">partial</span>(<span class="pl-s1">seats</span>,<span class="pl-s1">i</span>))</td>
        </tr>
        <tr>
          <td id="L302" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="302"></td>
          <td id="LC302" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>].<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">16</span>)</td>
        </tr>
        <tr>
          <td id="L303" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="303"></td>
          <td id="LC303" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span>(<span class="pl-s1">num</span><span class="pl-c1">==</span><span class="pl-c1">3</span>):</td>
        </tr>
        <tr>
          <td id="L304" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="304"></td>
          <td id="LC304" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-s1">pls</span>[<span class="pl-c1">3</span>]:</td>
        </tr>
        <tr>
          <td id="L305" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="305"></td>
          <td id="LC305" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>] <span class="pl-c1">=</span> <span class="pl-v">Button</span>(<span class="pl-s1">t</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s1">i</span>, <span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"Black"</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">"verdana"</span>,<span class="pl-c1">16</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">command</span><span class="pl-c1">=</span><span class="pl-en">partial</span>(<span class="pl-s1">seats</span>,<span class="pl-s1">i</span>))</td>
        </tr>
        <tr>
          <td id="L306" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="306"></td>
          <td id="LC306" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>].<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">16</span>)</td>
        </tr>
        <tr>
          <td id="L307" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="307"></td>
          <td id="LC307" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span>(<span class="pl-s1">num</span><span class="pl-c1">==</span><span class="pl-c1">4</span>):</td>
        </tr>
        <tr>
          <td id="L308" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="308"></td>
          <td id="LC308" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-s1">pls</span>[<span class="pl-c1">4</span>]:</td>
        </tr>
        <tr>
          <td id="L309" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="309"></td>
          <td id="LC309" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>] <span class="pl-c1">=</span> <span class="pl-v">Button</span>(<span class="pl-s1">t</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s1">i</span>, <span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"Black"</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">"verdana"</span>,<span class="pl-c1">16</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">command</span><span class="pl-c1">=</span><span class="pl-en">partial</span>(<span class="pl-s1">seats</span>,<span class="pl-s1">i</span>))</td>
        </tr>
        <tr>
          <td id="L310" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="310"></td>
          <td id="LC310" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>].<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">16</span>)</td>
        </tr>
        <tr>
          <td id="L311" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="311"></td>
          <td id="LC311" class="blob-code blob-code-inner js-file-line">            </td>
        </tr>
        <tr>
          <td id="L312" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="312"></td>
          <td id="LC312" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">drtimes</span>(<span class="pl-s1">num</span>,<span class="pl-s1">i</span>):</td>
        </tr>
        <tr>
          <td id="L313" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="313"></td>
          <td id="LC313" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">booking</span>[<span class="pl-s">'Theatre Name'</span>]<span class="pl-c1">=</span><span class="pl-s1">i</span></td>
        </tr>
        <tr>
          <td id="L314" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="314"></td>
          <td id="LC314" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">with</span> <span class="pl-en">open</span>(<span class="pl-s">'bookings.json'</span>,<span class="pl-s">'w'</span>) <span class="pl-k">as</span> <span class="pl-s1">file</span>:</td>
        </tr>
        <tr>
          <td id="L315" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="315"></td>
          <td id="LC315" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">json</span>.<span class="pl-en">dump</span>(<span class="pl-s1">booking</span>,<span class="pl-s1">file</span>)</td>
        </tr>
        <tr>
          <td id="L316" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="316"></td>
          <td id="LC316" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">t</span><span class="pl-c1">=</span><span class="pl-v">Tk</span>()</td>
        </tr>
        <tr>
          <td id="L317" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="317"></td>
          <td id="LC317" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">t</span>.<span class="pl-en">geometry</span>(<span class="pl-s">"1000x2000+10+20"</span>)</td>
        </tr>
        <tr>
          <td id="L318" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="318"></td>
          <td id="LC318" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">t</span>.<span class="pl-en">state</span>(<span class="pl-s">"zoomed"</span>)</td>
        </tr>
        <tr>
          <td id="L319" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="319"></td>
          <td id="LC319" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">t</span>[<span class="pl-s">'bg'</span>] <span class="pl-c1">=</span> <span class="pl-s">"deepskyblue"</span></td>
        </tr>
        <tr>
          <td id="L320" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="320"></td>
          <td id="LC320" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">heading</span> <span class="pl-c1">=</span> <span class="pl-v">Label</span>(<span class="pl-s1">t</span>,<span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s">"Timings"</span>,<span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">'verdana'</span>,<span class="pl-c1">25</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"black"</span>,<span class="pl-s1">bg</span><span class="pl-c1">=</span><span class="pl-s">"deepskyblue"</span>)</td>
        </tr>
        <tr>
          <td id="L321" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="321"></td>
          <td id="LC321" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">heading</span>.<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">10</span>)</td>
        </tr>
        <tr>
          <td id="L322" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="322"></td>
          <td id="LC322" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">style1</span> <span class="pl-c1">=</span> <span class="pl-v">Label</span>(<span class="pl-s1">t</span>,<span class="pl-s1">bg</span><span class="pl-c1">=</span><span class="pl-s">"black"</span>,<span class="pl-s1">height</span><span class="pl-c1">=</span><span class="pl-c1">1</span>,<span class="pl-s1">width</span><span class="pl-c1">=</span><span class="pl-c1">500</span>)</td>
        </tr>
        <tr>
          <td id="L323" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="323"></td>
          <td id="LC323" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">style1</span>.<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">10</span>)</td>
        </tr>
        <tr>
          <td id="L324" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="324"></td>
          <td id="LC324" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">button_dict</span><span class="pl-c1">=</span>{}</td>
        </tr>
        <tr>
          <td id="L325" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="325"></td>
          <td id="LC325" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">with</span> <span class="pl-en">open</span>(<span class="pl-s">"dr.json"</span>,<span class="pl-s">'r'</span>) <span class="pl-k">as</span> <span class="pl-s1">file</span>:</td>
        </tr>
        <tr>
          <td id="L326" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="326"></td>
          <td id="LC326" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">a</span><span class="pl-c1">=</span><span class="pl-s1">json</span>.<span class="pl-en">load</span>(<span class="pl-s1">file</span>)</td>
        </tr>
        <tr>
          <td id="L327" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="327"></td>
          <td id="LC327" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">pls</span><span class="pl-c1">=</span>[]</td>
        </tr>
        <tr>
          <td id="L328" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="328"></td>
          <td id="LC328" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-s1">a</span>.<span class="pl-en">values</span>():</td>
        </tr>
        <tr>
          <td id="L329" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="329"></td>
          <td id="LC329" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">pls</span>.<span class="pl-en">append</span>(<span class="pl-s1">i</span>)</td>
        </tr>
        <tr>
          <td id="L330" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="330"></td>
          <td id="LC330" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span>(<span class="pl-s1">num</span><span class="pl-c1">==</span><span class="pl-c1">0</span>):</td>
        </tr>
        <tr>
          <td id="L331" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="331"></td>
          <td id="LC331" class="blob-code blob-code-inner js-file-line">       <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-s1">pls</span>[<span class="pl-c1">0</span>]:</td>
        </tr>
        <tr>
          <td id="L332" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="332"></td>
          <td id="LC332" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>] <span class="pl-c1">=</span> <span class="pl-v">Button</span>(<span class="pl-s1">t</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s1">i</span>, <span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"Black"</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">"verdana"</span>,<span class="pl-c1">16</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">command</span><span class="pl-c1">=</span><span class="pl-en">partial</span>(<span class="pl-s1">seats</span>,<span class="pl-s1">i</span>))</td>
        </tr>
        <tr>
          <td id="L333" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="333"></td>
          <td id="LC333" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>].<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">16</span>)</td>
        </tr>
        <tr>
          <td id="L334" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="334"></td>
          <td id="LC334" class="blob-code blob-code-inner js-file-line">    </td>
        </tr>
        <tr>
          <td id="L335" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="335"></td>
          <td id="LC335" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span>(<span class="pl-s1">num</span><span class="pl-c1">==</span><span class="pl-c1">1</span>):</td>
        </tr>
        <tr>
          <td id="L336" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="336"></td>
          <td id="LC336" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-s1">pls</span>[<span class="pl-c1">1</span>]:</td>
        </tr>
        <tr>
          <td id="L337" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="337"></td>
          <td id="LC337" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>] <span class="pl-c1">=</span> <span class="pl-v">Button</span>(<span class="pl-s1">t</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s1">i</span>, <span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"Black"</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">"verdana"</span>,<span class="pl-c1">16</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">command</span><span class="pl-c1">=</span><span class="pl-en">partial</span>(<span class="pl-s1">seats</span>,<span class="pl-s1">i</span>))</td>
        </tr>
        <tr>
          <td id="L338" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="338"></td>
          <td id="LC338" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>].<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">16</span>)</td>
        </tr>
        <tr>
          <td id="L339" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="339"></td>
          <td id="LC339" class="blob-code blob-code-inner js-file-line">            </td>
        </tr>
        <tr>
          <td id="L340" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="340"></td>
          <td id="LC340" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span>(<span class="pl-s1">num</span><span class="pl-c1">==</span><span class="pl-c1">2</span>):</td>
        </tr>
        <tr>
          <td id="L341" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="341"></td>
          <td id="LC341" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-s1">pls</span>[<span class="pl-c1">2</span>]:</td>
        </tr>
        <tr>
          <td id="L342" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="342"></td>
          <td id="LC342" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>] <span class="pl-c1">=</span> <span class="pl-v">Button</span>(<span class="pl-s1">t</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s1">i</span>, <span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"Black"</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">"verdana"</span>,<span class="pl-c1">16</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">command</span><span class="pl-c1">=</span><span class="pl-en">partial</span>(<span class="pl-s1">seats</span>,<span class="pl-s1">i</span>))</td>
        </tr>
        <tr>
          <td id="L343" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="343"></td>
          <td id="LC343" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>].<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">16</span>)</td>
        </tr>
        <tr>
          <td id="L344" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="344"></td>
          <td id="LC344" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span>(<span class="pl-s1">num</span><span class="pl-c1">==</span><span class="pl-c1">3</span>):</td>
        </tr>
        <tr>
          <td id="L345" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="345"></td>
          <td id="LC345" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-s1">pls</span>[<span class="pl-c1">3</span>]:</td>
        </tr>
        <tr>
          <td id="L346" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="346"></td>
          <td id="LC346" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>] <span class="pl-c1">=</span> <span class="pl-v">Button</span>(<span class="pl-s1">t</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s1">i</span>, <span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"Black"</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">"verdana"</span>,<span class="pl-c1">16</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">command</span><span class="pl-c1">=</span><span class="pl-en">partial</span>(<span class="pl-s1">seats</span>,<span class="pl-s1">i</span>))</td>
        </tr>
        <tr>
          <td id="L347" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="347"></td>
          <td id="LC347" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>].<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">16</span>)</td>
        </tr>
        <tr>
          <td id="L348" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="348"></td>
          <td id="LC348" class="blob-code blob-code-inner js-file-line">            </td>
        </tr>
        <tr>
          <td id="L349" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="349"></td>
          <td id="LC349" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">samrattimes</span>(<span class="pl-s1">num</span>,<span class="pl-s1">i</span>):</td>
        </tr>
        <tr>
          <td id="L350" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="350"></td>
          <td id="LC350" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">booking</span>[<span class="pl-s">'Theatre Name'</span>]<span class="pl-c1">=</span><span class="pl-s1">i</span></td>
        </tr>
        <tr>
          <td id="L351" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="351"></td>
          <td id="LC351" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">with</span> <span class="pl-en">open</span>(<span class="pl-s">'bookings.json'</span>,<span class="pl-s">'w'</span>) <span class="pl-k">as</span> <span class="pl-s1">file</span>:</td>
        </tr>
        <tr>
          <td id="L352" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="352"></td>
          <td id="LC352" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">json</span>.<span class="pl-en">dump</span>(<span class="pl-s1">booking</span>,<span class="pl-s1">file</span>)</td>
        </tr>
        <tr>
          <td id="L353" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="353"></td>
          <td id="LC353" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">t</span><span class="pl-c1">=</span><span class="pl-v">Tk</span>()</td>
        </tr>
        <tr>
          <td id="L354" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="354"></td>
          <td id="LC354" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">t</span>.<span class="pl-en">geometry</span>(<span class="pl-s">"1000x2000+10+20"</span>)</td>
        </tr>
        <tr>
          <td id="L355" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="355"></td>
          <td id="LC355" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">t</span>.<span class="pl-en">state</span>(<span class="pl-s">"zoomed"</span>)</td>
        </tr>
        <tr>
          <td id="L356" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="356"></td>
          <td id="LC356" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">t</span>[<span class="pl-s">'bg'</span>] <span class="pl-c1">=</span> <span class="pl-s">"deepskyblue"</span></td>
        </tr>
        <tr>
          <td id="L357" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="357"></td>
          <td id="LC357" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">heading</span> <span class="pl-c1">=</span> <span class="pl-v">Label</span>(<span class="pl-s1">t</span>,<span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s">"Timings"</span>,<span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">'verdana'</span>,<span class="pl-c1">25</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"black"</span>,<span class="pl-s1">bg</span><span class="pl-c1">=</span><span class="pl-s">"deepskyblue"</span>)</td>
        </tr>
        <tr>
          <td id="L358" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="358"></td>
          <td id="LC358" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">heading</span>.<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">10</span>)</td>
        </tr>
        <tr>
          <td id="L359" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="359"></td>
          <td id="LC359" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">style1</span> <span class="pl-c1">=</span> <span class="pl-v">Label</span>(<span class="pl-s1">t</span>,<span class="pl-s1">bg</span><span class="pl-c1">=</span><span class="pl-s">"black"</span>,<span class="pl-s1">height</span><span class="pl-c1">=</span><span class="pl-c1">1</span>,<span class="pl-s1">width</span><span class="pl-c1">=</span><span class="pl-c1">500</span>)</td>
        </tr>
        <tr>
          <td id="L360" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="360"></td>
          <td id="LC360" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">style1</span>.<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">10</span>)</td>
        </tr>
        <tr>
          <td id="L361" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="361"></td>
          <td id="LC361" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">button_dict</span><span class="pl-c1">=</span>{}</td>
        </tr>
        <tr>
          <td id="L362" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="362"></td>
          <td id="LC362" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">with</span> <span class="pl-en">open</span>(<span class="pl-s">"samrat.json"</span>,<span class="pl-s">'r'</span>) <span class="pl-k">as</span> <span class="pl-s1">file</span>:</td>
        </tr>
        <tr>
          <td id="L363" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="363"></td>
          <td id="LC363" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">a</span><span class="pl-c1">=</span><span class="pl-s1">json</span>.<span class="pl-en">load</span>(<span class="pl-s1">file</span>)</td>
        </tr>
        <tr>
          <td id="L364" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="364"></td>
          <td id="LC364" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">pls</span><span class="pl-c1">=</span>[]</td>
        </tr>
        <tr>
          <td id="L365" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="365"></td>
          <td id="LC365" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-s1">a</span>.<span class="pl-en">values</span>():</td>
        </tr>
        <tr>
          <td id="L366" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="366"></td>
          <td id="LC366" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">pls</span>.<span class="pl-en">append</span>(<span class="pl-s1">i</span>)</td>
        </tr>
        <tr>
          <td id="L367" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="367"></td>
          <td id="LC367" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span>(<span class="pl-s1">num</span><span class="pl-c1">==</span><span class="pl-c1">0</span>):</td>
        </tr>
        <tr>
          <td id="L368" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="368"></td>
          <td id="LC368" class="blob-code blob-code-inner js-file-line">       <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-s1">pls</span>[<span class="pl-c1">0</span>]:</td>
        </tr>
        <tr>
          <td id="L369" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="369"></td>
          <td id="LC369" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>] <span class="pl-c1">=</span> <span class="pl-v">Button</span>(<span class="pl-s1">t</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s1">i</span>, <span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"Black"</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">"verdana"</span>,<span class="pl-c1">16</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">command</span><span class="pl-c1">=</span><span class="pl-en">partial</span>(<span class="pl-s1">seats</span>,<span class="pl-s1">i</span>))</td>
        </tr>
        <tr>
          <td id="L370" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="370"></td>
          <td id="LC370" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>].<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">16</span>)</td>
        </tr>
        <tr>
          <td id="L371" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="371"></td>
          <td id="LC371" class="blob-code blob-code-inner js-file-line">    </td>
        </tr>
        <tr>
          <td id="L372" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="372"></td>
          <td id="LC372" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span>(<span class="pl-s1">num</span><span class="pl-c1">==</span><span class="pl-c1">1</span>):</td>
        </tr>
        <tr>
          <td id="L373" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="373"></td>
          <td id="LC373" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-s1">pls</span>[<span class="pl-c1">1</span>]:</td>
        </tr>
        <tr>
          <td id="L374" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="374"></td>
          <td id="LC374" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>] <span class="pl-c1">=</span> <span class="pl-v">Button</span>(<span class="pl-s1">t</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s1">i</span>, <span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"Black"</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">"verdana"</span>,<span class="pl-c1">16</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">command</span><span class="pl-c1">=</span><span class="pl-en">partial</span>(<span class="pl-s1">seats</span>,<span class="pl-s1">i</span>))</td>
        </tr>
        <tr>
          <td id="L375" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="375"></td>
          <td id="LC375" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>].<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">16</span>)</td>
        </tr>
        <tr>
          <td id="L376" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="376"></td>
          <td id="LC376" class="blob-code blob-code-inner js-file-line">            </td>
        </tr>
        <tr>
          <td id="L377" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="377"></td>
          <td id="LC377" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span>(<span class="pl-s1">num</span><span class="pl-c1">==</span><span class="pl-c1">2</span>):</td>
        </tr>
        <tr>
          <td id="L378" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="378"></td>
          <td id="LC378" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-s1">pls</span>[<span class="pl-c1">2</span>]:</td>
        </tr>
        <tr>
          <td id="L379" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="379"></td>
          <td id="LC379" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>] <span class="pl-c1">=</span> <span class="pl-v">Button</span>(<span class="pl-s1">t</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s1">i</span>, <span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"Black"</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">"verdana"</span>,<span class="pl-c1">16</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">command</span><span class="pl-c1">=</span><span class="pl-en">partial</span>(<span class="pl-s1">seats</span>,<span class="pl-s1">i</span>))</td>
        </tr>
        <tr>
          <td id="L380" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="380"></td>
          <td id="LC380" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>].<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">16</span>)</td>
        </tr>
        <tr>
          <td id="L381" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="381"></td>
          <td id="LC381" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span>(<span class="pl-s1">num</span><span class="pl-c1">==</span><span class="pl-c1">3</span>):</td>
        </tr>
        <tr>
          <td id="L382" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="382"></td>
          <td id="LC382" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-s1">pls</span>[<span class="pl-c1">3</span>]:</td>
        </tr>
        <tr>
          <td id="L383" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="383"></td>
          <td id="LC383" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>] <span class="pl-c1">=</span> <span class="pl-v">Button</span>(<span class="pl-s1">t</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s1">i</span>, <span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"Black"</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">"verdana"</span>,<span class="pl-c1">16</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">command</span><span class="pl-c1">=</span><span class="pl-en">partial</span>(<span class="pl-s1">seats</span>,<span class="pl-s1">i</span>))</td>
        </tr>
        <tr>
          <td id="L384" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="384"></td>
          <td id="LC384" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>].<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">16</span>)</td>
        </tr>
        <tr>
          <td id="L385" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="385"></td>
          <td id="LC385" class="blob-code blob-code-inner js-file-line">            </td>
        </tr>
        <tr>
          <td id="L386" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="386"></td>
          <td id="LC386" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">janhittimes</span>(<span class="pl-s1">num</span>,<span class="pl-s1">i</span>):</td>
        </tr>
        <tr>
          <td id="L387" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="387"></td>
          <td id="LC387" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">booking</span>[<span class="pl-s">'Theatre Name'</span>]<span class="pl-c1">=</span><span class="pl-s1">i</span></td>
        </tr>
        <tr>
          <td id="L388" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="388"></td>
          <td id="LC388" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">with</span> <span class="pl-en">open</span>(<span class="pl-s">'bookings.json'</span>,<span class="pl-s">'w'</span>) <span class="pl-k">as</span> <span class="pl-s1">file</span>:</td>
        </tr>
        <tr>
          <td id="L389" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="389"></td>
          <td id="LC389" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">json</span>.<span class="pl-en">dump</span>(<span class="pl-s1">booking</span>,<span class="pl-s1">file</span>)</td>
        </tr>
        <tr>
          <td id="L390" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="390"></td>
          <td id="LC390" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">t</span><span class="pl-c1">=</span><span class="pl-v">Tk</span>()</td>
        </tr>
        <tr>
          <td id="L391" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="391"></td>
          <td id="LC391" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">t</span>.<span class="pl-en">geometry</span>(<span class="pl-s">"1000x2000+10+20"</span>)</td>
        </tr>
        <tr>
          <td id="L392" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="392"></td>
          <td id="LC392" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">t</span>.<span class="pl-en">state</span>(<span class="pl-s">"zoomed"</span>)</td>
        </tr>
        <tr>
          <td id="L393" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="393"></td>
          <td id="LC393" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">t</span>[<span class="pl-s">'bg'</span>] <span class="pl-c1">=</span> <span class="pl-s">"deepskyblue"</span></td>
        </tr>
        <tr>
          <td id="L394" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="394"></td>
          <td id="LC394" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">heading</span> <span class="pl-c1">=</span> <span class="pl-v">Label</span>(<span class="pl-s1">t</span>,<span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s">"Timings"</span>,<span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">'verdana'</span>,<span class="pl-c1">25</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"black"</span>,<span class="pl-s1">bg</span><span class="pl-c1">=</span><span class="pl-s">"deepskyblue"</span>)</td>
        </tr>
        <tr>
          <td id="L395" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="395"></td>
          <td id="LC395" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">heading</span>.<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">10</span>)</td>
        </tr>
        <tr>
          <td id="L396" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="396"></td>
          <td id="LC396" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">style1</span> <span class="pl-c1">=</span> <span class="pl-v">Label</span>(<span class="pl-s1">t</span>,<span class="pl-s1">bg</span><span class="pl-c1">=</span><span class="pl-s">"black"</span>,<span class="pl-s1">height</span><span class="pl-c1">=</span><span class="pl-c1">1</span>,<span class="pl-s1">width</span><span class="pl-c1">=</span><span class="pl-c1">500</span>)</td>
        </tr>
        <tr>
          <td id="L397" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="397"></td>
          <td id="LC397" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">style1</span>.<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">10</span>)</td>
        </tr>
        <tr>
          <td id="L398" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="398"></td>
          <td id="LC398" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">button_dict</span><span class="pl-c1">=</span>{}</td>
        </tr>
        <tr>
          <td id="L399" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="399"></td>
          <td id="LC399" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">with</span> <span class="pl-en">open</span>(<span class="pl-s">"janhit.json"</span>,<span class="pl-s">'r'</span>) <span class="pl-k">as</span> <span class="pl-s1">file</span>:</td>
        </tr>
        <tr>
          <td id="L400" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="400"></td>
          <td id="LC400" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">a</span><span class="pl-c1">=</span><span class="pl-s1">json</span>.<span class="pl-en">load</span>(<span class="pl-s1">file</span>)</td>
        </tr>
        <tr>
          <td id="L401" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="401"></td>
          <td id="LC401" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">pls</span><span class="pl-c1">=</span>[]</td>
        </tr>
        <tr>
          <td id="L402" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="402"></td>
          <td id="LC402" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-s1">a</span>.<span class="pl-en">values</span>():</td>
        </tr>
        <tr>
          <td id="L403" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="403"></td>
          <td id="LC403" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">pls</span>.<span class="pl-en">append</span>(<span class="pl-s1">i</span>)</td>
        </tr>
        <tr>
          <td id="L404" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="404"></td>
          <td id="LC404" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span>(<span class="pl-s1">num</span><span class="pl-c1">==</span><span class="pl-c1">0</span>):</td>
        </tr>
        <tr>
          <td id="L405" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="405"></td>
          <td id="LC405" class="blob-code blob-code-inner js-file-line">       <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-s1">pls</span>[<span class="pl-c1">0</span>]:</td>
        </tr>
        <tr>
          <td id="L406" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="406"></td>
          <td id="LC406" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>] <span class="pl-c1">=</span> <span class="pl-v">Button</span>(<span class="pl-s1">t</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s1">i</span>, <span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"Black"</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">"verdana"</span>,<span class="pl-c1">16</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">command</span><span class="pl-c1">=</span><span class="pl-en">partial</span>(<span class="pl-s1">seats</span>,<span class="pl-s1">i</span>))</td>
        </tr>
        <tr>
          <td id="L407" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="407"></td>
          <td id="LC407" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>].<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">16</span>)</td>
        </tr>
        <tr>
          <td id="L408" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="408"></td>
          <td id="LC408" class="blob-code blob-code-inner js-file-line">    </td>
        </tr>
        <tr>
          <td id="L409" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="409"></td>
          <td id="LC409" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span>(<span class="pl-s1">num</span><span class="pl-c1">==</span><span class="pl-c1">1</span>):</td>
        </tr>
        <tr>
          <td id="L410" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="410"></td>
          <td id="LC410" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-s1">pls</span>[<span class="pl-c1">1</span>]:</td>
        </tr>
        <tr>
          <td id="L411" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="411"></td>
          <td id="LC411" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>] <span class="pl-c1">=</span> <span class="pl-v">Button</span>(<span class="pl-s1">t</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s1">i</span>, <span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"Black"</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">"verdana"</span>,<span class="pl-c1">16</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">command</span><span class="pl-c1">=</span><span class="pl-en">partial</span>(<span class="pl-s1">seats</span>,<span class="pl-s1">i</span>))</td>
        </tr>
        <tr>
          <td id="L412" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="412"></td>
          <td id="LC412" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>].<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">16</span>)</td>
        </tr>
        <tr>
          <td id="L413" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="413"></td>
          <td id="LC413" class="blob-code blob-code-inner js-file-line">            </td>
        </tr>
        <tr>
          <td id="L414" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="414"></td>
          <td id="LC414" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span>(<span class="pl-s1">num</span><span class="pl-c1">==</span><span class="pl-c1">2</span>):</td>
        </tr>
        <tr>
          <td id="L415" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="415"></td>
          <td id="LC415" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-s1">pls</span>[<span class="pl-c1">2</span>]:</td>
        </tr>
        <tr>
          <td id="L416" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="416"></td>
          <td id="LC416" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>] <span class="pl-c1">=</span> <span class="pl-v">Button</span>(<span class="pl-s1">t</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s1">i</span>, <span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"Black"</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">"verdana"</span>,<span class="pl-c1">16</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">command</span><span class="pl-c1">=</span><span class="pl-en">partial</span>(<span class="pl-s1">seats</span>,<span class="pl-s1">i</span>))</td>
        </tr>
        <tr>
          <td id="L417" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="417"></td>
          <td id="LC417" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>].<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">16</span>)</td>
        </tr>
        <tr>
          <td id="L418" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="418"></td>
          <td id="LC418" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span>(<span class="pl-s1">num</span><span class="pl-c1">==</span><span class="pl-c1">3</span>):</td>
        </tr>
        <tr>
          <td id="L419" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="419"></td>
          <td id="LC419" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-s1">pls</span>[<span class="pl-c1">3</span>]:</td>
        </tr>
        <tr>
          <td id="L420" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="420"></td>
          <td id="LC420" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>] <span class="pl-c1">=</span> <span class="pl-v">Button</span>(<span class="pl-s1">t</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s1">i</span>, <span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"Black"</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">"verdana"</span>,<span class="pl-c1">16</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">command</span><span class="pl-c1">=</span><span class="pl-en">partial</span>(<span class="pl-s1">seats</span>,<span class="pl-s1">i</span>))</td>
        </tr>
        <tr>
          <td id="L421" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="421"></td>
          <td id="LC421" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>].<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">16</span>)</td>
        </tr>
        <tr>
          <td id="L422" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="422"></td>
          <td id="LC422" class="blob-code blob-code-inner js-file-line">            </td>
        </tr>
        <tr>
          <td id="L423" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="423"></td>
          <td id="LC423" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">antetimes</span>(<span class="pl-s1">num</span>,<span class="pl-s1">i</span>):</td>
        </tr>
        <tr>
          <td id="L424" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="424"></td>
          <td id="LC424" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">booking</span>[<span class="pl-s">'Theatre Name'</span>]<span class="pl-c1">=</span><span class="pl-s1">i</span></td>
        </tr>
        <tr>
          <td id="L425" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="425"></td>
          <td id="LC425" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">with</span> <span class="pl-en">open</span>(<span class="pl-s">'bookings.json'</span>,<span class="pl-s">'w'</span>) <span class="pl-k">as</span> <span class="pl-s1">file</span>:</td>
        </tr>
        <tr>
          <td id="L426" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="426"></td>
          <td id="LC426" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">json</span>.<span class="pl-en">dump</span>(<span class="pl-s1">booking</span>,<span class="pl-s1">file</span>)</td>
        </tr>
        <tr>
          <td id="L427" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="427"></td>
          <td id="LC427" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">t</span><span class="pl-c1">=</span><span class="pl-v">Tk</span>()</td>
        </tr>
        <tr>
          <td id="L428" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="428"></td>
          <td id="LC428" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">t</span>.<span class="pl-en">geometry</span>(<span class="pl-s">"1000x2000+10+20"</span>)</td>
        </tr>
        <tr>
          <td id="L429" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="429"></td>
          <td id="LC429" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">t</span>.<span class="pl-en">state</span>(<span class="pl-s">"zoomed"</span>)</td>
        </tr>
        <tr>
          <td id="L430" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="430"></td>
          <td id="LC430" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">t</span>[<span class="pl-s">'bg'</span>] <span class="pl-c1">=</span> <span class="pl-s">"deepskyblue"</span></td>
        </tr>
        <tr>
          <td id="L431" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="431"></td>
          <td id="LC431" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">heading</span> <span class="pl-c1">=</span> <span class="pl-v">Label</span>(<span class="pl-s1">t</span>,<span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s">"Timings"</span>,<span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">'verdana'</span>,<span class="pl-c1">25</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"black"</span>,<span class="pl-s1">bg</span><span class="pl-c1">=</span><span class="pl-s">"deepskyblue"</span>)</td>
        </tr>
        <tr>
          <td id="L432" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="432"></td>
          <td id="LC432" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">heading</span>.<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">10</span>)</td>
        </tr>
        <tr>
          <td id="L433" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="433"></td>
          <td id="LC433" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">style1</span> <span class="pl-c1">=</span> <span class="pl-v">Label</span>(<span class="pl-s1">t</span>,<span class="pl-s1">bg</span><span class="pl-c1">=</span><span class="pl-s">"black"</span>,<span class="pl-s1">height</span><span class="pl-c1">=</span><span class="pl-c1">1</span>,<span class="pl-s1">width</span><span class="pl-c1">=</span><span class="pl-c1">500</span>)</td>
        </tr>
        <tr>
          <td id="L434" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="434"></td>
          <td id="LC434" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">style1</span>.<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">10</span>)</td>
        </tr>
        <tr>
          <td id="L435" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="435"></td>
          <td id="LC435" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">button_dict</span><span class="pl-c1">=</span>{}</td>
        </tr>
        <tr>
          <td id="L436" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="436"></td>
          <td id="LC436" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">with</span> <span class="pl-en">open</span>(<span class="pl-s">"ante.json"</span>,<span class="pl-s">'r'</span>) <span class="pl-k">as</span> <span class="pl-s1">file</span>:</td>
        </tr>
        <tr>
          <td id="L437" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="437"></td>
          <td id="LC437" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">a</span><span class="pl-c1">=</span><span class="pl-s1">json</span>.<span class="pl-en">load</span>(<span class="pl-s1">file</span>)</td>
        </tr>
        <tr>
          <td id="L438" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="438"></td>
          <td id="LC438" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">pls</span><span class="pl-c1">=</span>[]</td>
        </tr>
        <tr>
          <td id="L439" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="439"></td>
          <td id="LC439" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-s1">a</span>.<span class="pl-en">values</span>():</td>
        </tr>
        <tr>
          <td id="L440" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="440"></td>
          <td id="LC440" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">pls</span>.<span class="pl-en">append</span>(<span class="pl-s1">i</span>)</td>
        </tr>
        <tr>
          <td id="L441" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="441"></td>
          <td id="LC441" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span>(<span class="pl-s1">num</span><span class="pl-c1">==</span><span class="pl-c1">0</span>):</td>
        </tr>
        <tr>
          <td id="L442" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="442"></td>
          <td id="LC442" class="blob-code blob-code-inner js-file-line">       <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-s1">pls</span>[<span class="pl-c1">0</span>]:</td>
        </tr>
        <tr>
          <td id="L443" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="443"></td>
          <td id="LC443" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>] <span class="pl-c1">=</span> <span class="pl-v">Button</span>(<span class="pl-s1">t</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s1">i</span>, <span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"Black"</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">"verdana"</span>,<span class="pl-c1">16</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">command</span><span class="pl-c1">=</span><span class="pl-en">partial</span>(<span class="pl-s1">seats</span>,<span class="pl-s1">i</span>))</td>
        </tr>
        <tr>
          <td id="L444" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="444"></td>
          <td id="LC444" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>].<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">16</span>)</td>
        </tr>
        <tr>
          <td id="L445" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="445"></td>
          <td id="LC445" class="blob-code blob-code-inner js-file-line">    </td>
        </tr>
        <tr>
          <td id="L446" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="446"></td>
          <td id="LC446" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span>(<span class="pl-s1">num</span><span class="pl-c1">==</span><span class="pl-c1">1</span>):</td>
        </tr>
        <tr>
          <td id="L447" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="447"></td>
          <td id="LC447" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-s1">pls</span>[<span class="pl-c1">1</span>]:</td>
        </tr>
        <tr>
          <td id="L448" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="448"></td>
          <td id="LC448" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>] <span class="pl-c1">=</span> <span class="pl-v">Button</span>(<span class="pl-s1">t</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s1">i</span>, <span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"Black"</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">"verdana"</span>,<span class="pl-c1">16</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">command</span><span class="pl-c1">=</span><span class="pl-en">partial</span>(<span class="pl-s1">seats</span>,<span class="pl-s1">i</span>))</td>
        </tr>
        <tr>
          <td id="L449" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="449"></td>
          <td id="LC449" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>].<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">16</span>)</td>
        </tr>
        <tr>
          <td id="L450" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="450"></td>
          <td id="LC450" class="blob-code blob-code-inner js-file-line">            </td>
        </tr>
        <tr>
          <td id="L451" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="451"></td>
          <td id="LC451" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span>(<span class="pl-s1">num</span><span class="pl-c1">==</span><span class="pl-c1">2</span>):</td>
        </tr>
        <tr>
          <td id="L452" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="452"></td>
          <td id="LC452" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-s1">pls</span>[<span class="pl-c1">2</span>]:</td>
        </tr>
        <tr>
          <td id="L453" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="453"></td>
          <td id="LC453" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>] <span class="pl-c1">=</span> <span class="pl-v">Button</span>(<span class="pl-s1">t</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s1">i</span>, <span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"Black"</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">"verdana"</span>,<span class="pl-c1">16</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">command</span><span class="pl-c1">=</span><span class="pl-en">partial</span>(<span class="pl-s1">seats</span>,<span class="pl-s1">i</span>))</td>
        </tr>
        <tr>
          <td id="L454" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="454"></td>
          <td id="LC454" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>].<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">16</span>)</td>
        </tr>
        <tr>
          <td id="L455" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="455"></td>
          <td id="LC455" class="blob-code blob-code-inner js-file-line">            </td>
        </tr>
        <tr>
          <td id="L456" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="456"></td>
          <td id="LC456" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">majortimes</span>(<span class="pl-s1">num</span>,<span class="pl-s1">i</span>):</td>
        </tr>
        <tr>
          <td id="L457" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="457"></td>
          <td id="LC457" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">booking</span>[<span class="pl-s">'Theatre Name'</span>]<span class="pl-c1">=</span><span class="pl-s1">i</span></td>
        </tr>
        <tr>
          <td id="L458" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="458"></td>
          <td id="LC458" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">with</span> <span class="pl-en">open</span>(<span class="pl-s">'bookings.json'</span>,<span class="pl-s">'w'</span>) <span class="pl-k">as</span> <span class="pl-s1">file</span>:</td>
        </tr>
        <tr>
          <td id="L459" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="459"></td>
          <td id="LC459" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">json</span>.<span class="pl-en">dump</span>(<span class="pl-s1">booking</span>,<span class="pl-s1">file</span>)</td>
        </tr>
        <tr>
          <td id="L460" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="460"></td>
          <td id="LC460" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">t</span><span class="pl-c1">=</span><span class="pl-v">Tk</span>()</td>
        </tr>
        <tr>
          <td id="L461" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="461"></td>
          <td id="LC461" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">t</span>.<span class="pl-en">geometry</span>(<span class="pl-s">"1000x2000+10+20"</span>)</td>
        </tr>
        <tr>
          <td id="L462" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="462"></td>
          <td id="LC462" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">t</span>.<span class="pl-en">state</span>(<span class="pl-s">"zoomed"</span>)</td>
        </tr>
        <tr>
          <td id="L463" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="463"></td>
          <td id="LC463" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">t</span>[<span class="pl-s">'bg'</span>] <span class="pl-c1">=</span> <span class="pl-s">"deepskyblue"</span></td>
        </tr>
        <tr>
          <td id="L464" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="464"></td>
          <td id="LC464" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">heading</span> <span class="pl-c1">=</span> <span class="pl-v">Label</span>(<span class="pl-s1">t</span>,<span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s">"Timings"</span>,<span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">'verdana'</span>,<span class="pl-c1">25</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"black"</span>,<span class="pl-s1">bg</span><span class="pl-c1">=</span><span class="pl-s">"deepskyblue"</span>)</td>
        </tr>
        <tr>
          <td id="L465" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="465"></td>
          <td id="LC465" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">heading</span>.<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">10</span>)</td>
        </tr>
        <tr>
          <td id="L466" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="466"></td>
          <td id="LC466" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">style1</span> <span class="pl-c1">=</span> <span class="pl-v">Label</span>(<span class="pl-s1">t</span>,<span class="pl-s1">bg</span><span class="pl-c1">=</span><span class="pl-s">"black"</span>,<span class="pl-s1">height</span><span class="pl-c1">=</span><span class="pl-c1">1</span>,<span class="pl-s1">width</span><span class="pl-c1">=</span><span class="pl-c1">500</span>)</td>
        </tr>
        <tr>
          <td id="L467" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="467"></td>
          <td id="LC467" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">style1</span>.<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">10</span>)</td>
        </tr>
        <tr>
          <td id="L468" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="468"></td>
          <td id="LC468" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">button_dict</span><span class="pl-c1">=</span>{}</td>
        </tr>
        <tr>
          <td id="L469" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="469"></td>
          <td id="LC469" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">with</span> <span class="pl-en">open</span>(<span class="pl-s">"major.json"</span>,<span class="pl-s">'r'</span>) <span class="pl-k">as</span> <span class="pl-s1">file</span>:</td>
        </tr>
        <tr>
          <td id="L470" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="470"></td>
          <td id="LC470" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">a</span><span class="pl-c1">=</span><span class="pl-s1">json</span>.<span class="pl-en">load</span>(<span class="pl-s1">file</span>)</td>
        </tr>
        <tr>
          <td id="L471" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="471"></td>
          <td id="LC471" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">pls</span><span class="pl-c1">=</span>[]</td>
        </tr>
        <tr>
          <td id="L472" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="472"></td>
          <td id="LC472" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-s1">a</span>.<span class="pl-en">values</span>():</td>
        </tr>
        <tr>
          <td id="L473" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="473"></td>
          <td id="LC473" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">pls</span>.<span class="pl-en">append</span>(<span class="pl-s1">i</span>)</td>
        </tr>
        <tr>
          <td id="L474" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="474"></td>
          <td id="LC474" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span>(<span class="pl-s1">num</span><span class="pl-c1">==</span><span class="pl-c1">0</span>):</td>
        </tr>
        <tr>
          <td id="L475" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="475"></td>
          <td id="LC475" class="blob-code blob-code-inner js-file-line">       <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-s1">pls</span>[<span class="pl-c1">0</span>]:</td>
        </tr>
        <tr>
          <td id="L476" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="476"></td>
          <td id="LC476" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>] <span class="pl-c1">=</span> <span class="pl-v">Button</span>(<span class="pl-s1">t</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s1">i</span>, <span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"Black"</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">"verdana"</span>,<span class="pl-c1">16</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">command</span><span class="pl-c1">=</span><span class="pl-en">partial</span>(<span class="pl-s1">seats</span>,<span class="pl-s1">i</span>))</td>
        </tr>
        <tr>
          <td id="L477" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="477"></td>
          <td id="LC477" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>].<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">16</span>)</td>
        </tr>
        <tr>
          <td id="L478" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="478"></td>
          <td id="LC478" class="blob-code blob-code-inner js-file-line">    </td>
        </tr>
        <tr>
          <td id="L479" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="479"></td>
          <td id="LC479" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span>(<span class="pl-s1">num</span><span class="pl-c1">==</span><span class="pl-c1">1</span>):</td>
        </tr>
        <tr>
          <td id="L480" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="480"></td>
          <td id="LC480" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-s1">pls</span>[<span class="pl-c1">1</span>]:</td>
        </tr>
        <tr>
          <td id="L481" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="481"></td>
          <td id="LC481" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>] <span class="pl-c1">=</span> <span class="pl-v">Button</span>(<span class="pl-s1">t</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s1">i</span>, <span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"Black"</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">"verdana"</span>,<span class="pl-c1">16</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">command</span><span class="pl-c1">=</span><span class="pl-en">partial</span>(<span class="pl-s1">seats</span>,<span class="pl-s1">i</span>))</td>
        </tr>
        <tr>
          <td id="L482" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="482"></td>
          <td id="LC482" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>].<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">16</span>)</td>
        </tr>
        <tr>
          <td id="L483" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="483"></td>
          <td id="LC483" class="blob-code blob-code-inner js-file-line">            </td>
        </tr>
        <tr>
          <td id="L484" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="484"></td>
          <td id="LC484" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span>(<span class="pl-s1">num</span><span class="pl-c1">==</span><span class="pl-c1">2</span>):</td>
        </tr>
        <tr>
          <td id="L485" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="485"></td>
          <td id="LC485" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-s1">pls</span>[<span class="pl-c1">2</span>]:</td>
        </tr>
        <tr>
          <td id="L486" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="486"></td>
          <td id="LC486" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>] <span class="pl-c1">=</span> <span class="pl-v">Button</span>(<span class="pl-s1">t</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s1">i</span>, <span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"Black"</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">"verdana"</span>,<span class="pl-c1">16</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">command</span><span class="pl-c1">=</span><span class="pl-en">partial</span>(<span class="pl-s1">seats</span>,<span class="pl-s1">i</span>))</td>
        </tr>
        <tr>
          <td id="L487" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="487"></td>
          <td id="LC487" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>].<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">16</span>)</td>
        </tr>
        <tr>
          <td id="L488" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="488"></td>
          <td id="LC488" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span>(<span class="pl-s1">num</span><span class="pl-c1">==</span><span class="pl-c1">3</span>):</td>
        </tr>
        <tr>
          <td id="L489" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="489"></td>
          <td id="LC489" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-s1">pls</span>[<span class="pl-c1">3</span>]:</td>
        </tr>
        <tr>
          <td id="L490" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="490"></td>
          <td id="LC490" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>] <span class="pl-c1">=</span> <span class="pl-v">Button</span>(<span class="pl-s1">t</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s1">i</span>, <span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"Black"</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">"verdana"</span>,<span class="pl-c1">16</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">command</span><span class="pl-c1">=</span><span class="pl-en">partial</span>(<span class="pl-s1">seats</span>,<span class="pl-s1">i</span>))</td>
        </tr>
        <tr>
          <td id="L491" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="491"></td>
          <td id="LC491" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>].<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">16</span>)</td>
        </tr>
        <tr>
          <td id="L492" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="492"></td>
          <td id="LC492" class="blob-code blob-code-inner js-file-line">    </td>
        </tr>
        <tr>
          <td id="L493" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="493"></td>
          <td id="LC493" class="blob-code blob-code-inner js-file-line">
</td>
        </tr>
        <tr>
          <td id="L494" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="494"></td>
          <td id="LC494" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">tamilmovies</span>(<span class="pl-s1">num</span>,<span class="pl-s1">name</span>):</td>
        </tr>
        <tr>
          <td id="L495" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="495"></td>
          <td id="LC495" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">booking</span>[<span class="pl-s">'Name of Movie'</span>]<span class="pl-c1">=</span><span class="pl-s1">name</span></td>
        </tr>
        <tr>
          <td id="L496" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="496"></td>
          <td id="LC496" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">with</span> <span class="pl-en">open</span>(<span class="pl-s">'bookings.json'</span>,<span class="pl-s">'w'</span>) <span class="pl-k">as</span> <span class="pl-s1">file</span>:</td>
        </tr>
        <tr>
          <td id="L497" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="497"></td>
          <td id="LC497" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">json</span>.<span class="pl-en">dump</span>(<span class="pl-s1">booking</span>,<span class="pl-s1">file</span>)</td>
        </tr>
        <tr>
          <td id="L498" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="498"></td>
          <td id="LC498" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">t</span><span class="pl-c1">=</span><span class="pl-v">Tk</span>()</td>
        </tr>
        <tr>
          <td id="L499" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="499"></td>
          <td id="LC499" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">t</span>.<span class="pl-en">geometry</span>(<span class="pl-s">"1000x2000+10+20"</span>)</td>
        </tr>
        <tr>
          <td id="L500" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="500"></td>
          <td id="LC500" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">t</span>.<span class="pl-en">state</span>(<span class="pl-s">"zoomed"</span>)</td>
        </tr>
        <tr>
          <td id="L501" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="501"></td>
          <td id="LC501" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">t</span>[<span class="pl-s">'bg'</span>] <span class="pl-c1">=</span> <span class="pl-s">"deepskyblue"</span></td>
        </tr>
        <tr>
          <td id="L502" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="502"></td>
          <td id="LC502" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> <span class="pl-s1">num</span><span class="pl-c1">==</span><span class="pl-c1">0</span>:</td>
        </tr>
        <tr>
          <td id="L503" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="503"></td>
          <td id="LC503" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">heading</span> <span class="pl-c1">=</span> <span class="pl-v">Label</span>(<span class="pl-s1">t</span>,<span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s">"Vikram (movie theatres)"</span>,<span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">'verdana'</span>,<span class="pl-c1">25</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"black"</span>,<span class="pl-s1">bg</span><span class="pl-c1">=</span><span class="pl-s">"deepskyblue"</span>)</td>
        </tr>
        <tr>
          <td id="L504" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="504"></td>
          <td id="LC504" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">heading</span>.<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">10</span>)</td>
        </tr>
        <tr>
          <td id="L505" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="505"></td>
          <td id="LC505" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">style1</span> <span class="pl-c1">=</span> <span class="pl-v">Label</span>(<span class="pl-s1">t</span>,<span class="pl-s1">bg</span><span class="pl-c1">=</span><span class="pl-s">"black"</span>,<span class="pl-s1">height</span><span class="pl-c1">=</span><span class="pl-c1">1</span>,<span class="pl-s1">width</span><span class="pl-c1">=</span><span class="pl-c1">500</span>)</td>
        </tr>
        <tr>
          <td id="L506" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="506"></td>
          <td id="LC506" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">style1</span>.<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">10</span>)</td>
        </tr>
        <tr>
          <td id="L507" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="507"></td>
          <td id="LC507" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">button_dict</span><span class="pl-c1">=</span>{}</td>
        </tr>
        <tr>
          <td id="L508" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="508"></td>
          <td id="LC508" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">with</span> <span class="pl-en">open</span>(<span class="pl-s">"vikram.json"</span>,<span class="pl-s">'r'</span>) <span class="pl-k">as</span> <span class="pl-s1">file</span>:</td>
        </tr>
        <tr>
          <td id="L509" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="509"></td>
          <td id="LC509" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">a</span><span class="pl-c1">=</span><span class="pl-s1">json</span>.<span class="pl-en">load</span>(<span class="pl-s1">file</span>)</td>
        </tr>
        <tr>
          <td id="L510" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="510"></td>
          <td id="LC510" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">b</span><span class="pl-c1">=</span><span class="pl-c1">0</span></td>
        </tr>
        <tr>
          <td id="L511" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="511"></td>
          <td id="LC511" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-en">list</span>(<span class="pl-s1">a</span>.<span class="pl-en">keys</span>()):</td>
        </tr>
        <tr>
          <td id="L512" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="512"></td>
          <td id="LC512" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>] <span class="pl-c1">=</span> <span class="pl-v">Button</span>(<span class="pl-s1">t</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s1">i</span>, <span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"Black"</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">"verdana"</span>,<span class="pl-c1">16</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">command</span><span class="pl-c1">=</span><span class="pl-en">partial</span>(<span class="pl-s1">vikramtimes</span>,<span class="pl-s1">b</span>,<span class="pl-s1">i</span>))</td>
        </tr>
        <tr>
          <td id="L513" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="513"></td>
          <td id="LC513" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>].<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">16</span>)</td>
        </tr>
        <tr>
          <td id="L514" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="514"></td>
          <td id="LC514" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">b</span><span class="pl-c1">=</span><span class="pl-s1">b</span><span class="pl-c1">+</span><span class="pl-c1">1</span></td>
        </tr>
        <tr>
          <td id="L515" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="515"></td>
          <td id="LC515" class="blob-code blob-code-inner js-file-line">    </td>
        </tr>
        <tr>
          <td id="L516" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="516"></td>
          <td id="LC516" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">elif</span> <span class="pl-s1">num</span><span class="pl-c1">==</span><span class="pl-c1">1</span>:</td>
        </tr>
        <tr>
          <td id="L517" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="517"></td>
          <td id="LC517" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">heading</span> <span class="pl-c1">=</span> <span class="pl-v">Label</span>(<span class="pl-s1">t</span>,<span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s">"Jurassic World: Dominion (movie theatres)"</span>,<span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">'verdana'</span>,<span class="pl-c1">25</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"black"</span>,<span class="pl-s1">bg</span><span class="pl-c1">=</span><span class="pl-s">"deepskyblue"</span>)</td>
        </tr>
        <tr>
          <td id="L518" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="518"></td>
          <td id="LC518" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">heading</span>.<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">10</span>)</td>
        </tr>
        <tr>
          <td id="L519" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="519"></td>
          <td id="LC519" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">style1</span> <span class="pl-c1">=</span> <span class="pl-v">Label</span>(<span class="pl-s1">t</span>,<span class="pl-s1">bg</span><span class="pl-c1">=</span><span class="pl-s">"black"</span>,<span class="pl-s1">height</span><span class="pl-c1">=</span><span class="pl-c1">1</span>,<span class="pl-s1">width</span><span class="pl-c1">=</span><span class="pl-c1">500</span>)</td>
        </tr>
        <tr>
          <td id="L520" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="520"></td>
          <td id="LC520" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">style1</span>.<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">10</span>)</td>
        </tr>
        <tr>
          <td id="L521" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="521"></td>
          <td id="LC521" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">button_dict</span><span class="pl-c1">=</span>{}</td>
        </tr>
        <tr>
          <td id="L522" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="522"></td>
          <td id="LC522" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">with</span> <span class="pl-en">open</span>(<span class="pl-s">"jurassic.json"</span>,<span class="pl-s">'r'</span>) <span class="pl-k">as</span> <span class="pl-s1">file</span>:</td>
        </tr>
        <tr>
          <td id="L523" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="523"></td>
          <td id="LC523" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">a</span><span class="pl-c1">=</span><span class="pl-s1">json</span>.<span class="pl-en">load</span>(<span class="pl-s1">file</span>)</td>
        </tr>
        <tr>
          <td id="L524" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="524"></td>
          <td id="LC524" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">b</span><span class="pl-c1">=</span><span class="pl-c1">0</span></td>
        </tr>
        <tr>
          <td id="L525" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="525"></td>
          <td id="LC525" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-en">list</span>(<span class="pl-s1">a</span>.<span class="pl-en">keys</span>()):</td>
        </tr>
        <tr>
          <td id="L526" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="526"></td>
          <td id="LC526" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>] <span class="pl-c1">=</span> <span class="pl-v">Button</span>(<span class="pl-s1">t</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s1">i</span>, <span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"Black"</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">"verdana"</span>,<span class="pl-c1">16</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">command</span><span class="pl-c1">=</span><span class="pl-en">partial</span>(<span class="pl-s1">jurassictimes</span>,<span class="pl-s1">b</span>,<span class="pl-s1">i</span>))</td>
        </tr>
        <tr>
          <td id="L527" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="527"></td>
          <td id="LC527" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>].<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">16</span>)</td>
        </tr>
        <tr>
          <td id="L528" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="528"></td>
          <td id="LC528" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">b</span><span class="pl-c1">=</span><span class="pl-s1">b</span><span class="pl-c1">+</span><span class="pl-c1">1</span></td>
        </tr>
        <tr>
          <td id="L529" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="529"></td>
          <td id="LC529" class="blob-code blob-code-inner js-file-line">            </td>
        </tr>
        <tr>
          <td id="L530" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="530"></td>
          <td id="LC530" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">elif</span> <span class="pl-s1">num</span><span class="pl-c1">==</span><span class="pl-c1">2</span>:</td>
        </tr>
        <tr>
          <td id="L531" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="531"></td>
          <td id="LC531" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">heading</span> <span class="pl-c1">=</span> <span class="pl-v">Label</span>(<span class="pl-s1">t</span>,<span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s">"777 Charlie (movie theatres)"</span>,<span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">'verdana'</span>,<span class="pl-c1">25</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"black"</span>,<span class="pl-s1">bg</span><span class="pl-c1">=</span><span class="pl-s">"deepskyblue"</span>)</td>
        </tr>
        <tr>
          <td id="L532" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="532"></td>
          <td id="LC532" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">heading</span>.<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">10</span>)</td>
        </tr>
        <tr>
          <td id="L533" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="533"></td>
          <td id="LC533" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">style1</span> <span class="pl-c1">=</span> <span class="pl-v">Label</span>(<span class="pl-s1">t</span>,<span class="pl-s1">bg</span><span class="pl-c1">=</span><span class="pl-s">"black"</span>,<span class="pl-s1">height</span><span class="pl-c1">=</span><span class="pl-c1">1</span>,<span class="pl-s1">width</span><span class="pl-c1">=</span><span class="pl-c1">500</span>)</td>
        </tr>
        <tr>
          <td id="L534" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="534"></td>
          <td id="LC534" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">style1</span>.<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">10</span>)</td>
        </tr>
        <tr>
          <td id="L535" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="535"></td>
          <td id="LC535" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">button_dict</span><span class="pl-c1">=</span>{}</td>
        </tr>
        <tr>
          <td id="L536" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="536"></td>
          <td id="LC536" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">with</span> <span class="pl-en">open</span>(<span class="pl-s">"charlie.json"</span>,<span class="pl-s">'r'</span>) <span class="pl-k">as</span> <span class="pl-s1">file</span>:</td>
        </tr>
        <tr>
          <td id="L537" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="537"></td>
          <td id="LC537" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">a</span><span class="pl-c1">=</span><span class="pl-s1">json</span>.<span class="pl-en">load</span>(<span class="pl-s1">file</span>)</td>
        </tr>
        <tr>
          <td id="L538" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="538"></td>
          <td id="LC538" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">b</span><span class="pl-c1">=</span><span class="pl-c1">0</span></td>
        </tr>
        <tr>
          <td id="L539" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="539"></td>
          <td id="LC539" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-en">list</span>(<span class="pl-s1">a</span>.<span class="pl-en">keys</span>()):</td>
        </tr>
        <tr>
          <td id="L540" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="540"></td>
          <td id="LC540" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>] <span class="pl-c1">=</span> <span class="pl-v">Button</span>(<span class="pl-s1">t</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s1">i</span>, <span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"Black"</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">"verdana"</span>,<span class="pl-c1">16</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">command</span><span class="pl-c1">=</span><span class="pl-en">partial</span>(<span class="pl-s1">charlietimes</span>,<span class="pl-s1">b</span>,<span class="pl-s1">i</span>))</td>
        </tr>
        <tr>
          <td id="L541" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="541"></td>
          <td id="LC541" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>].<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">16</span>)</td>
        </tr>
        <tr>
          <td id="L542" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="542"></td>
          <td id="LC542" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">b</span><span class="pl-c1">=</span><span class="pl-s1">b</span><span class="pl-c1">+</span><span class="pl-c1">1</span></td>
        </tr>
        <tr>
          <td id="L543" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="543"></td>
          <td id="LC543" class="blob-code blob-code-inner js-file-line">    </td>
        </tr>
        <tr>
          <td id="L544" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="544"></td>
          <td id="LC544" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">elif</span> <span class="pl-s1">num</span><span class="pl-c1">==</span><span class="pl-c1">3</span>:</td>
        </tr>
        <tr>
          <td id="L545" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="545"></td>
          <td id="LC545" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">heading</span> <span class="pl-c1">=</span> <span class="pl-v">Label</span>(<span class="pl-s1">t</span>,<span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s">"Don (movie theatres)"</span>,<span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">'verdana'</span>,<span class="pl-c1">25</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"black"</span>,<span class="pl-s1">bg</span><span class="pl-c1">=</span><span class="pl-s">"deepskyblue"</span>)</td>
        </tr>
        <tr>
          <td id="L546" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="546"></td>
          <td id="LC546" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">heading</span>.<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">10</span>)</td>
        </tr>
        <tr>
          <td id="L547" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="547"></td>
          <td id="LC547" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">style1</span> <span class="pl-c1">=</span> <span class="pl-v">Label</span>(<span class="pl-s1">t</span>,<span class="pl-s1">bg</span><span class="pl-c1">=</span><span class="pl-s">"black"</span>,<span class="pl-s1">height</span><span class="pl-c1">=</span><span class="pl-c1">1</span>,<span class="pl-s1">width</span><span class="pl-c1">=</span><span class="pl-c1">500</span>)</td>
        </tr>
        <tr>
          <td id="L548" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="548"></td>
          <td id="LC548" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">style1</span>.<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">10</span>)</td>
        </tr>
        <tr>
          <td id="L549" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="549"></td>
          <td id="LC549" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">button_dict</span><span class="pl-c1">=</span>{}</td>
        </tr>
        <tr>
          <td id="L550" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="550"></td>
          <td id="LC550" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">with</span> <span class="pl-en">open</span>(<span class="pl-s">"don.json"</span>,<span class="pl-s">'r'</span>) <span class="pl-k">as</span> <span class="pl-s1">file</span>:</td>
        </tr>
        <tr>
          <td id="L551" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="551"></td>
          <td id="LC551" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">a</span><span class="pl-c1">=</span><span class="pl-s1">json</span>.<span class="pl-en">load</span>(<span class="pl-s1">file</span>)</td>
        </tr>
        <tr>
          <td id="L552" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="552"></td>
          <td id="LC552" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">b</span><span class="pl-c1">=</span><span class="pl-c1">0</span></td>
        </tr>
        <tr>
          <td id="L553" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="553"></td>
          <td id="LC553" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-en">list</span>(<span class="pl-s1">a</span>.<span class="pl-en">keys</span>()):</td>
        </tr>
        <tr>
          <td id="L554" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="554"></td>
          <td id="LC554" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>] <span class="pl-c1">=</span> <span class="pl-v">Button</span>(<span class="pl-s1">t</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s1">i</span>, <span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"Black"</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">"verdana"</span>,<span class="pl-c1">16</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">command</span><span class="pl-c1">=</span><span class="pl-en">partial</span>(<span class="pl-s1">dontimes</span>,<span class="pl-s1">b</span>,<span class="pl-s1">i</span>))</td>
        </tr>
        <tr>
          <td id="L555" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="555"></td>
          <td id="LC555" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>].<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">16</span>)</td>
        </tr>
        <tr>
          <td id="L556" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="556"></td>
          <td id="LC556" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">b</span><span class="pl-c1">=</span><span class="pl-s1">b</span><span class="pl-c1">+</span><span class="pl-c1">1</span></td>
        </tr>
        <tr>
          <td id="L557" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="557"></td>
          <td id="LC557" class="blob-code blob-code-inner js-file-line">            </td>
        </tr>
        <tr>
          <td id="L558" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="558"></td>
          <td id="LC558" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">elif</span> <span class="pl-s1">num</span><span class="pl-c1">==</span><span class="pl-c1">4</span>:</td>
        </tr>
        <tr>
          <td id="L559" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="559"></td>
          <td id="LC559" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">heading</span> <span class="pl-c1">=</span> <span class="pl-v">Label</span>(<span class="pl-s1">t</span>,<span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s">"Adade Sundara (movie theatres)"</span>,<span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">'verdana'</span>,<span class="pl-c1">25</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"black"</span>,<span class="pl-s1">bg</span><span class="pl-c1">=</span><span class="pl-s">"deepskyblue"</span>)</td>
        </tr>
        <tr>
          <td id="L560" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="560"></td>
          <td id="LC560" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">heading</span>.<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">10</span>)</td>
        </tr>
        <tr>
          <td id="L561" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="561"></td>
          <td id="LC561" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">style1</span> <span class="pl-c1">=</span> <span class="pl-v">Label</span>(<span class="pl-s1">t</span>,<span class="pl-s1">bg</span><span class="pl-c1">=</span><span class="pl-s">"black"</span>,<span class="pl-s1">height</span><span class="pl-c1">=</span><span class="pl-c1">1</span>,<span class="pl-s1">width</span><span class="pl-c1">=</span><span class="pl-c1">500</span>)</td>
        </tr>
        <tr>
          <td id="L562" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="562"></td>
          <td id="LC562" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">style1</span>.<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">10</span>)</td>
        </tr>
        <tr>
          <td id="L563" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="563"></td>
          <td id="LC563" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">button_dict</span><span class="pl-c1">=</span>{}</td>
        </tr>
        <tr>
          <td id="L564" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="564"></td>
          <td id="LC564" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">with</span> <span class="pl-en">open</span>(<span class="pl-s">"adade.json"</span>,<span class="pl-s">'r'</span>) <span class="pl-k">as</span> <span class="pl-s1">file</span>:</td>
        </tr>
        <tr>
          <td id="L565" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="565"></td>
          <td id="LC565" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">a</span><span class="pl-c1">=</span><span class="pl-s1">json</span>.<span class="pl-en">load</span>(<span class="pl-s1">file</span>)</td>
        </tr>
        <tr>
          <td id="L566" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="566"></td>
          <td id="LC566" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">b</span><span class="pl-c1">=</span><span class="pl-c1">0</span></td>
        </tr>
        <tr>
          <td id="L567" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="567"></td>
          <td id="LC567" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-en">list</span>(<span class="pl-s1">a</span>.<span class="pl-en">keys</span>()):</td>
        </tr>
        <tr>
          <td id="L568" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="568"></td>
          <td id="LC568" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>] <span class="pl-c1">=</span> <span class="pl-v">Button</span>(<span class="pl-s1">t</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s1">i</span>, <span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"Black"</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">"verdana"</span>,<span class="pl-c1">16</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">command</span><span class="pl-c1">=</span><span class="pl-en">partial</span>(<span class="pl-s1">adadetimes</span>,<span class="pl-s1">b</span>,<span class="pl-s1">i</span>))</td>
        </tr>
        <tr>
          <td id="L569" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="569"></td>
          <td id="LC569" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>].<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">16</span>)   </td>
        </tr>
        <tr>
          <td id="L570" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="570"></td>
          <td id="LC570" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">b</span><span class="pl-c1">=</span><span class="pl-s1">b</span><span class="pl-c1">+</span><span class="pl-c1">1</span></td>
        </tr>
        <tr>
          <td id="L571" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="571"></td>
          <td id="LC571" class="blob-code blob-code-inner js-file-line">
</td>
        </tr>
        <tr>
          <td id="L572" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="572"></td>
          <td id="LC572" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">englishmovies</span>(<span class="pl-s1">num</span>,<span class="pl-s1">name</span>):</td>
        </tr>
        <tr>
          <td id="L573" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="573"></td>
          <td id="LC573" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">booking</span>[<span class="pl-s">'Name of Movie'</span>]<span class="pl-c1">=</span><span class="pl-s1">name</span></td>
        </tr>
        <tr>
          <td id="L574" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="574"></td>
          <td id="LC574" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">with</span> <span class="pl-en">open</span>(<span class="pl-s">'bookings.json'</span>,<span class="pl-s">'w'</span>) <span class="pl-k">as</span> <span class="pl-s1">file</span>:</td>
        </tr>
        <tr>
          <td id="L575" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="575"></td>
          <td id="LC575" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">json</span>.<span class="pl-en">dump</span>(<span class="pl-s1">booking</span>,<span class="pl-s1">file</span>)</td>
        </tr>
        <tr>
          <td id="L576" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="576"></td>
          <td id="LC576" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">t</span><span class="pl-c1">=</span><span class="pl-v">Tk</span>()</td>
        </tr>
        <tr>
          <td id="L577" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="577"></td>
          <td id="LC577" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">t</span>.<span class="pl-en">geometry</span>(<span class="pl-s">"1000x2000+10+20"</span>)</td>
        </tr>
        <tr>
          <td id="L578" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="578"></td>
          <td id="LC578" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">t</span>.<span class="pl-en">state</span>(<span class="pl-s">"zoomed"</span>)</td>
        </tr>
        <tr>
          <td id="L579" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="579"></td>
          <td id="LC579" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">t</span>[<span class="pl-s">'bg'</span>] <span class="pl-c1">=</span> <span class="pl-s">"deepskyblue"</span></td>
        </tr>
        <tr>
          <td id="L580" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="580"></td>
          <td id="LC580" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> <span class="pl-s1">num</span><span class="pl-c1">==</span><span class="pl-c1">0</span>:</td>
        </tr>
        <tr>
          <td id="L581" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="581"></td>
          <td id="LC581" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">heading</span> <span class="pl-c1">=</span> <span class="pl-v">Label</span>(<span class="pl-s1">t</span>,<span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s">"Jurassic World: Dominion (movie theatres)"</span>,<span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">'verdana'</span>,<span class="pl-c1">25</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"black"</span>,<span class="pl-s1">bg</span><span class="pl-c1">=</span><span class="pl-s">"deepskyblue"</span>)</td>
        </tr>
        <tr>
          <td id="L582" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="582"></td>
          <td id="LC582" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">heading</span>.<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">10</span>)</td>
        </tr>
        <tr>
          <td id="L583" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="583"></td>
          <td id="LC583" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">style1</span> <span class="pl-c1">=</span> <span class="pl-v">Label</span>(<span class="pl-s1">t</span>,<span class="pl-s1">bg</span><span class="pl-c1">=</span><span class="pl-s">"black"</span>,<span class="pl-s1">height</span><span class="pl-c1">=</span><span class="pl-c1">1</span>,<span class="pl-s1">width</span><span class="pl-c1">=</span><span class="pl-c1">500</span>)</td>
        </tr>
        <tr>
          <td id="L584" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="584"></td>
          <td id="LC584" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">style1</span>.<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">10</span>)</td>
        </tr>
        <tr>
          <td id="L585" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="585"></td>
          <td id="LC585" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">button_dict</span><span class="pl-c1">=</span>{}</td>
        </tr>
        <tr>
          <td id="L586" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="586"></td>
          <td id="LC586" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">with</span> <span class="pl-en">open</span>(<span class="pl-s">"ejurassic.json"</span>,<span class="pl-s">'r'</span>) <span class="pl-k">as</span> <span class="pl-s1">file</span>:</td>
        </tr>
        <tr>
          <td id="L587" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="587"></td>
          <td id="LC587" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">a</span><span class="pl-c1">=</span><span class="pl-s1">json</span>.<span class="pl-en">load</span>(<span class="pl-s1">file</span>)</td>
        </tr>
        <tr>
          <td id="L588" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="588"></td>
          <td id="LC588" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">b</span><span class="pl-c1">=</span><span class="pl-c1">0</span></td>
        </tr>
        <tr>
          <td id="L589" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="589"></td>
          <td id="LC589" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-en">list</span>(<span class="pl-s1">a</span>.<span class="pl-en">keys</span>()):</td>
        </tr>
        <tr>
          <td id="L590" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="590"></td>
          <td id="LC590" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>] <span class="pl-c1">=</span> <span class="pl-v">Button</span>(<span class="pl-s1">t</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s1">i</span>, <span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"Black"</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">"verdana"</span>,<span class="pl-c1">16</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">command</span><span class="pl-c1">=</span><span class="pl-en">partial</span>(<span class="pl-s1">ejurassictimes</span>,<span class="pl-s1">b</span>,<span class="pl-s1">i</span>))</td>
        </tr>
        <tr>
          <td id="L591" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="591"></td>
          <td id="LC591" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>].<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">16</span>)</td>
        </tr>
        <tr>
          <td id="L592" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="592"></td>
          <td id="LC592" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">b</span><span class="pl-c1">=</span><span class="pl-s1">b</span><span class="pl-c1">+</span><span class="pl-c1">1</span></td>
        </tr>
        <tr>
          <td id="L593" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="593"></td>
          <td id="LC593" class="blob-code blob-code-inner js-file-line">    </td>
        </tr>
        <tr>
          <td id="L594" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="594"></td>
          <td id="LC594" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">elif</span> <span class="pl-s1">num</span><span class="pl-c1">==</span><span class="pl-c1">1</span>:</td>
        </tr>
        <tr>
          <td id="L595" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="595"></td>
          <td id="LC595" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">heading</span> <span class="pl-c1">=</span> <span class="pl-v">Label</span>(<span class="pl-s1">t</span>,<span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s">"Top Gun: Maverick (movie theatres)"</span>,<span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">'verdana'</span>,<span class="pl-c1">25</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"black"</span>,<span class="pl-s1">bg</span><span class="pl-c1">=</span><span class="pl-s">"deepskyblue"</span>)</td>
        </tr>
        <tr>
          <td id="L596" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="596"></td>
          <td id="LC596" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">heading</span>.<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">10</span>)</td>
        </tr>
        <tr>
          <td id="L597" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="597"></td>
          <td id="LC597" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">style1</span> <span class="pl-c1">=</span> <span class="pl-v">Label</span>(<span class="pl-s1">t</span>,<span class="pl-s1">bg</span><span class="pl-c1">=</span><span class="pl-s">"black"</span>,<span class="pl-s1">height</span><span class="pl-c1">=</span><span class="pl-c1">1</span>,<span class="pl-s1">width</span><span class="pl-c1">=</span><span class="pl-c1">500</span>)</td>
        </tr>
        <tr>
          <td id="L598" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="598"></td>
          <td id="LC598" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">style1</span>.<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">10</span>)</td>
        </tr>
        <tr>
          <td id="L599" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="599"></td>
          <td id="LC599" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">button_dict</span><span class="pl-c1">=</span>{}</td>
        </tr>
        <tr>
          <td id="L600" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="600"></td>
          <td id="LC600" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">with</span> <span class="pl-en">open</span>(<span class="pl-s">"topgun.json"</span>,<span class="pl-s">'r'</span>) <span class="pl-k">as</span> <span class="pl-s1">file</span>:</td>
        </tr>
        <tr>
          <td id="L601" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="601"></td>
          <td id="LC601" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">a</span><span class="pl-c1">=</span><span class="pl-s1">json</span>.<span class="pl-en">load</span>(<span class="pl-s1">file</span>)</td>
        </tr>
        <tr>
          <td id="L602" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="602"></td>
          <td id="LC602" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">b</span><span class="pl-c1">=</span><span class="pl-c1">0</span></td>
        </tr>
        <tr>
          <td id="L603" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="603"></td>
          <td id="LC603" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-en">list</span>(<span class="pl-s1">a</span>.<span class="pl-en">keys</span>()):</td>
        </tr>
        <tr>
          <td id="L604" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="604"></td>
          <td id="LC604" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>] <span class="pl-c1">=</span> <span class="pl-v">Button</span>(<span class="pl-s1">t</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s1">i</span>, <span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"Black"</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">"verdana"</span>,<span class="pl-c1">16</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">command</span><span class="pl-c1">=</span><span class="pl-en">partial</span>(<span class="pl-s1">topguntimes</span>,<span class="pl-s1">b</span>,<span class="pl-s1">i</span>))</td>
        </tr>
        <tr>
          <td id="L605" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="605"></td>
          <td id="LC605" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>].<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">16</span>)</td>
        </tr>
        <tr>
          <td id="L606" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="606"></td>
          <td id="LC606" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">b</span><span class="pl-c1">=</span><span class="pl-s1">b</span><span class="pl-c1">+</span><span class="pl-c1">1</span></td>
        </tr>
        <tr>
          <td id="L607" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="607"></td>
          <td id="LC607" class="blob-code blob-code-inner js-file-line">            </td>
        </tr>
        <tr>
          <td id="L608" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="608"></td>
          <td id="LC608" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">elif</span> <span class="pl-s1">num</span><span class="pl-c1">==</span><span class="pl-c1">2</span>:</td>
        </tr>
        <tr>
          <td id="L609" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="609"></td>
          <td id="LC609" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">heading</span> <span class="pl-c1">=</span> <span class="pl-v">Label</span>(<span class="pl-s1">t</span>,<span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s">"Doctor Strange: In The Multiverse Of Madness (movie theatres)"</span>,<span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">'verdana'</span>,<span class="pl-c1">25</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"black"</span>,<span class="pl-s1">bg</span><span class="pl-c1">=</span><span class="pl-s">"deepskyblue"</span>)</td>
        </tr>
        <tr>
          <td id="L610" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="610"></td>
          <td id="LC610" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">heading</span>.<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">10</span>)</td>
        </tr>
        <tr>
          <td id="L611" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="611"></td>
          <td id="LC611" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">style1</span> <span class="pl-c1">=</span> <span class="pl-v">Label</span>(<span class="pl-s1">t</span>,<span class="pl-s1">bg</span><span class="pl-c1">=</span><span class="pl-s">"black"</span>,<span class="pl-s1">height</span><span class="pl-c1">=</span><span class="pl-c1">1</span>,<span class="pl-s1">width</span><span class="pl-c1">=</span><span class="pl-c1">500</span>)</td>
        </tr>
        <tr>
          <td id="L612" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="612"></td>
          <td id="LC612" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">style1</span>.<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">10</span>)</td>
        </tr>
        <tr>
          <td id="L613" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="613"></td>
          <td id="LC613" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">button_dict</span><span class="pl-c1">=</span>{}</td>
        </tr>
        <tr>
          <td id="L614" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="614"></td>
          <td id="LC614" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">with</span> <span class="pl-en">open</span>(<span class="pl-s">"dr.json"</span>,<span class="pl-s">'r'</span>) <span class="pl-k">as</span> <span class="pl-s1">file</span>:</td>
        </tr>
        <tr>
          <td id="L615" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="615"></td>
          <td id="LC615" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">a</span><span class="pl-c1">=</span><span class="pl-s1">json</span>.<span class="pl-en">load</span>(<span class="pl-s1">file</span>)</td>
        </tr>
        <tr>
          <td id="L616" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="616"></td>
          <td id="LC616" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">b</span><span class="pl-c1">=</span><span class="pl-c1">0</span></td>
        </tr>
        <tr>
          <td id="L617" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="617"></td>
          <td id="LC617" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-en">list</span>(<span class="pl-s1">a</span>.<span class="pl-en">keys</span>()):</td>
        </tr>
        <tr>
          <td id="L618" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="618"></td>
          <td id="LC618" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>] <span class="pl-c1">=</span> <span class="pl-v">Button</span>(<span class="pl-s1">t</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s1">i</span>, <span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"Black"</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">"verdana"</span>,<span class="pl-c1">16</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">command</span><span class="pl-c1">=</span><span class="pl-en">partial</span>(<span class="pl-s1">drtimes</span>,<span class="pl-s1">b</span>,<span class="pl-s1">i</span>))</td>
        </tr>
        <tr>
          <td id="L619" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="619"></td>
          <td id="LC619" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>].<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">16</span>)</td>
        </tr>
        <tr>
          <td id="L620" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="620"></td>
          <td id="LC620" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">b</span><span class="pl-c1">=</span><span class="pl-s1">b</span><span class="pl-c1">+</span><span class="pl-c1">1</span></td>
        </tr>
        <tr>
          <td id="L621" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="621"></td>
          <td id="LC621" class="blob-code blob-code-inner js-file-line">            </td>
        </tr>
        <tr>
          <td id="L622" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="622"></td>
          <td id="LC622" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">hindimovies</span>(<span class="pl-s1">num</span>,<span class="pl-s1">name</span>):</td>
        </tr>
        <tr>
          <td id="L623" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="623"></td>
          <td id="LC623" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">booking</span>[<span class="pl-s">'Name of Movie'</span>]<span class="pl-c1">=</span><span class="pl-s1">name</span></td>
        </tr>
        <tr>
          <td id="L624" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="624"></td>
          <td id="LC624" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">with</span> <span class="pl-en">open</span>(<span class="pl-s">'bookings.json'</span>,<span class="pl-s">'w'</span>) <span class="pl-k">as</span> <span class="pl-s1">file</span>:</td>
        </tr>
        <tr>
          <td id="L625" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="625"></td>
          <td id="LC625" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">json</span>.<span class="pl-en">dump</span>(<span class="pl-s1">booking</span>,<span class="pl-s1">file</span>)</td>
        </tr>
        <tr>
          <td id="L626" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="626"></td>
          <td id="LC626" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">t</span><span class="pl-c1">=</span><span class="pl-v">Tk</span>()</td>
        </tr>
        <tr>
          <td id="L627" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="627"></td>
          <td id="LC627" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">t</span>.<span class="pl-en">geometry</span>(<span class="pl-s">"1000x2000+10+20"</span>)</td>
        </tr>
        <tr>
          <td id="L628" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="628"></td>
          <td id="LC628" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">t</span>.<span class="pl-en">state</span>(<span class="pl-s">"zoomed"</span>)</td>
        </tr>
        <tr>
          <td id="L629" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="629"></td>
          <td id="LC629" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">t</span>[<span class="pl-s">'bg'</span>] <span class="pl-c1">=</span> <span class="pl-s">"deepskyblue"</span></td>
        </tr>
        <tr>
          <td id="L630" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="630"></td>
          <td id="LC630" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> <span class="pl-s1">num</span><span class="pl-c1">==</span><span class="pl-c1">0</span>:</td>
        </tr>
        <tr>
          <td id="L631" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="631"></td>
          <td id="LC631" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">heading</span> <span class="pl-c1">=</span> <span class="pl-v">Label</span>(<span class="pl-s1">t</span>,<span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s">"Samrat Prithviraj (movie theatres)"</span>,<span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">'verdana'</span>,<span class="pl-c1">25</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"black"</span>,<span class="pl-s1">bg</span><span class="pl-c1">=</span><span class="pl-s">"deepskyblue"</span>)</td>
        </tr>
        <tr>
          <td id="L632" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="632"></td>
          <td id="LC632" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">heading</span>.<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">10</span>)</td>
        </tr>
        <tr>
          <td id="L633" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="633"></td>
          <td id="LC633" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">style1</span> <span class="pl-c1">=</span> <span class="pl-v">Label</span>(<span class="pl-s1">t</span>,<span class="pl-s1">bg</span><span class="pl-c1">=</span><span class="pl-s">"black"</span>,<span class="pl-s1">height</span><span class="pl-c1">=</span><span class="pl-c1">1</span>,<span class="pl-s1">width</span><span class="pl-c1">=</span><span class="pl-c1">500</span>)</td>
        </tr>
        <tr>
          <td id="L634" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="634"></td>
          <td id="LC634" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">style1</span>.<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">10</span>)</td>
        </tr>
        <tr>
          <td id="L635" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="635"></td>
          <td id="LC635" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">button_dict</span><span class="pl-c1">=</span>{}</td>
        </tr>
        <tr>
          <td id="L636" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="636"></td>
          <td id="LC636" class="blob-code blob-code-inner js-file-line">        </td>
        </tr>
        <tr>
          <td id="L637" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="637"></td>
          <td id="LC637" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">with</span> <span class="pl-en">open</span>(<span class="pl-s">"samrat.json"</span>,<span class="pl-s">'r'</span>) <span class="pl-k">as</span> <span class="pl-s1">file</span>:</td>
        </tr>
        <tr>
          <td id="L638" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="638"></td>
          <td id="LC638" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">a</span><span class="pl-c1">=</span><span class="pl-s1">json</span>.<span class="pl-en">load</span>(<span class="pl-s1">file</span>)</td>
        </tr>
        <tr>
          <td id="L639" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="639"></td>
          <td id="LC639" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">b</span><span class="pl-c1">=</span><span class="pl-c1">0</span></td>
        </tr>
        <tr>
          <td id="L640" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="640"></td>
          <td id="LC640" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-en">list</span>(<span class="pl-s1">a</span>.<span class="pl-en">keys</span>()):</td>
        </tr>
        <tr>
          <td id="L641" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="641"></td>
          <td id="LC641" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>] <span class="pl-c1">=</span> <span class="pl-v">Button</span>(<span class="pl-s1">t</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s1">i</span>, <span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"Black"</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">"verdana"</span>,<span class="pl-c1">16</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">command</span><span class="pl-c1">=</span><span class="pl-en">partial</span>(<span class="pl-s1">samrattimes</span>,<span class="pl-s1">b</span>,<span class="pl-s1">i</span>))</td>
        </tr>
        <tr>
          <td id="L642" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="642"></td>
          <td id="LC642" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>].<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">16</span>)</td>
        </tr>
        <tr>
          <td id="L643" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="643"></td>
          <td id="LC643" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">b</span><span class="pl-c1">=</span><span class="pl-s1">b</span><span class="pl-c1">+</span><span class="pl-c1">1</span></td>
        </tr>
        <tr>
          <td id="L644" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="644"></td>
          <td id="LC644" class="blob-code blob-code-inner js-file-line">    </td>
        </tr>
        <tr>
          <td id="L645" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="645"></td>
          <td id="LC645" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">elif</span> <span class="pl-s1">num</span><span class="pl-c1">==</span><span class="pl-c1">1</span>:</td>
        </tr>
        <tr>
          <td id="L646" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="646"></td>
          <td id="LC646" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">heading</span> <span class="pl-c1">=</span> <span class="pl-v">Label</span>(<span class="pl-s1">t</span>,<span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s">"Janhit Mein Jaari (movie theatres)"</span>,<span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">'verdana'</span>,<span class="pl-c1">25</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"black"</span>,<span class="pl-s1">bg</span><span class="pl-c1">=</span><span class="pl-s">"deepskyblue"</span>)</td>
        </tr>
        <tr>
          <td id="L647" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="647"></td>
          <td id="LC647" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">heading</span>.<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">10</span>)</td>
        </tr>
        <tr>
          <td id="L648" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="648"></td>
          <td id="LC648" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">style1</span> <span class="pl-c1">=</span> <span class="pl-v">Label</span>(<span class="pl-s1">t</span>,<span class="pl-s1">bg</span><span class="pl-c1">=</span><span class="pl-s">"black"</span>,<span class="pl-s1">height</span><span class="pl-c1">=</span><span class="pl-c1">1</span>,<span class="pl-s1">width</span><span class="pl-c1">=</span><span class="pl-c1">500</span>)</td>
        </tr>
        <tr>
          <td id="L649" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="649"></td>
          <td id="LC649" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">style1</span>.<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">10</span>)</td>
        </tr>
        <tr>
          <td id="L650" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="650"></td>
          <td id="LC650" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">button_dict</span><span class="pl-c1">=</span>{}</td>
        </tr>
        <tr>
          <td id="L651" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="651"></td>
          <td id="LC651" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">with</span> <span class="pl-en">open</span>(<span class="pl-s">"janhit.json"</span>,<span class="pl-s">'r'</span>) <span class="pl-k">as</span> <span class="pl-s1">file</span>:</td>
        </tr>
        <tr>
          <td id="L652" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="652"></td>
          <td id="LC652" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">a</span><span class="pl-c1">=</span><span class="pl-s1">json</span>.<span class="pl-en">load</span>(<span class="pl-s1">file</span>)</td>
        </tr>
        <tr>
          <td id="L653" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="653"></td>
          <td id="LC653" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">b</span><span class="pl-c1">=</span><span class="pl-c1">0</span></td>
        </tr>
        <tr>
          <td id="L654" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="654"></td>
          <td id="LC654" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-en">list</span>(<span class="pl-s1">a</span>.<span class="pl-en">keys</span>()):</td>
        </tr>
        <tr>
          <td id="L655" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="655"></td>
          <td id="LC655" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>] <span class="pl-c1">=</span> <span class="pl-v">Button</span>(<span class="pl-s1">t</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s1">i</span>, <span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"Black"</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">"verdana"</span>,<span class="pl-c1">16</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">command</span><span class="pl-c1">=</span><span class="pl-en">partial</span>(<span class="pl-s1">janhittimes</span>,<span class="pl-s1">b</span>,<span class="pl-s1">i</span>))</td>
        </tr>
        <tr>
          <td id="L656" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="656"></td>
          <td id="LC656" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>].<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">16</span>)</td>
        </tr>
        <tr>
          <td id="L657" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="657"></td>
          <td id="LC657" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">b</span><span class="pl-c1">=</span><span class="pl-s1">b</span><span class="pl-c1">+</span><span class="pl-c1">1</span></td>
        </tr>
        <tr>
          <td id="L658" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="658"></td>
          <td id="LC658" class="blob-code blob-code-inner js-file-line">            </td>
        </tr>
        <tr>
          <td id="L659" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="659"></td>
          <td id="LC659" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">telugumovies</span>(<span class="pl-s1">num</span>,<span class="pl-s1">name</span>):</td>
        </tr>
        <tr>
          <td id="L660" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="660"></td>
          <td id="LC660" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">booking</span>[<span class="pl-s">'Name of Movie'</span>]<span class="pl-c1">=</span><span class="pl-s1">name</span></td>
        </tr>
        <tr>
          <td id="L661" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="661"></td>
          <td id="LC661" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">with</span> <span class="pl-en">open</span>(<span class="pl-s">'bookings.json'</span>,<span class="pl-s">'w'</span>) <span class="pl-k">as</span> <span class="pl-s1">file</span>:</td>
        </tr>
        <tr>
          <td id="L662" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="662"></td>
          <td id="LC662" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">json</span>.<span class="pl-en">dump</span>(<span class="pl-s1">booking</span>,<span class="pl-s1">file</span>)</td>
        </tr>
        <tr>
          <td id="L663" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="663"></td>
          <td id="LC663" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">t</span><span class="pl-c1">=</span><span class="pl-v">Tk</span>()</td>
        </tr>
        <tr>
          <td id="L664" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="664"></td>
          <td id="LC664" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">t</span>.<span class="pl-en">geometry</span>(<span class="pl-s">"1000x2000+10+20"</span>)</td>
        </tr>
        <tr>
          <td id="L665" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="665"></td>
          <td id="LC665" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">t</span>.<span class="pl-en">state</span>(<span class="pl-s">"zoomed"</span>)</td>
        </tr>
        <tr>
          <td id="L666" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="666"></td>
          <td id="LC666" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">t</span>[<span class="pl-s">'bg'</span>] <span class="pl-c1">=</span> <span class="pl-s">"deepskyblue"</span></td>
        </tr>
        <tr>
          <td id="L667" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="667"></td>
          <td id="LC667" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> <span class="pl-s1">num</span><span class="pl-c1">==</span><span class="pl-c1">0</span>:</td>
        </tr>
        <tr>
          <td id="L668" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="668"></td>
          <td id="LC668" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">heading</span> <span class="pl-c1">=</span> <span class="pl-v">Label</span>(<span class="pl-s1">t</span>,<span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s">"Ante Sundaraniki (movie theatres)"</span>,<span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">'verdana'</span>,<span class="pl-c1">25</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"black"</span>,<span class="pl-s1">bg</span><span class="pl-c1">=</span><span class="pl-s">"deepskyblue"</span>)</td>
        </tr>
        <tr>
          <td id="L669" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="669"></td>
          <td id="LC669" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">heading</span>.<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">10</span>)</td>
        </tr>
        <tr>
          <td id="L670" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="670"></td>
          <td id="LC670" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">style1</span> <span class="pl-c1">=</span> <span class="pl-v">Label</span>(<span class="pl-s1">t</span>,<span class="pl-s1">bg</span><span class="pl-c1">=</span><span class="pl-s">"black"</span>,<span class="pl-s1">height</span><span class="pl-c1">=</span><span class="pl-c1">1</span>,<span class="pl-s1">width</span><span class="pl-c1">=</span><span class="pl-c1">500</span>)</td>
        </tr>
        <tr>
          <td id="L671" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="671"></td>
          <td id="LC671" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">style1</span>.<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">10</span>)</td>
        </tr>
        <tr>
          <td id="L672" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="672"></td>
          <td id="LC672" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">button_dict</span><span class="pl-c1">=</span>{}</td>
        </tr>
        <tr>
          <td id="L673" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="673"></td>
          <td id="LC673" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">with</span> <span class="pl-en">open</span>(<span class="pl-s">"ante.json"</span>,<span class="pl-s">'r'</span>) <span class="pl-k">as</span> <span class="pl-s1">file</span>:</td>
        </tr>
        <tr>
          <td id="L674" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="674"></td>
          <td id="LC674" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">a</span><span class="pl-c1">=</span><span class="pl-s1">json</span>.<span class="pl-en">load</span>(<span class="pl-s1">file</span>)</td>
        </tr>
        <tr>
          <td id="L675" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="675"></td>
          <td id="LC675" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">b</span><span class="pl-c1">=</span><span class="pl-c1">0</span></td>
        </tr>
        <tr>
          <td id="L676" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="676"></td>
          <td id="LC676" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-en">list</span>(<span class="pl-s1">a</span>.<span class="pl-en">keys</span>()):</td>
        </tr>
        <tr>
          <td id="L677" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="677"></td>
          <td id="LC677" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>] <span class="pl-c1">=</span> <span class="pl-v">Button</span>(<span class="pl-s1">t</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s1">i</span>, <span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"Black"</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">"verdana"</span>,<span class="pl-c1">16</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">command</span><span class="pl-c1">=</span><span class="pl-en">partial</span>(<span class="pl-s1">antetimes</span>,<span class="pl-s1">b</span>,<span class="pl-s1">i</span>))</td>
        </tr>
        <tr>
          <td id="L678" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="678"></td>
          <td id="LC678" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>].<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">16</span>)</td>
        </tr>
        <tr>
          <td id="L679" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="679"></td>
          <td id="LC679" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">b</span><span class="pl-c1">=</span><span class="pl-s1">b</span><span class="pl-c1">+</span><span class="pl-c1">1</span></td>
        </tr>
        <tr>
          <td id="L680" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="680"></td>
          <td id="LC680" class="blob-code blob-code-inner js-file-line">    </td>
        </tr>
        <tr>
          <td id="L681" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="681"></td>
          <td id="LC681" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">elif</span> <span class="pl-s1">num</span><span class="pl-c1">==</span><span class="pl-c1">1</span>:</td>
        </tr>
        <tr>
          <td id="L682" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="682"></td>
          <td id="LC682" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">heading</span> <span class="pl-c1">=</span> <span class="pl-v">Label</span>(<span class="pl-s1">t</span>,<span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s">"MAJOR (movie theatres)"</span>,<span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">'verdana'</span>,<span class="pl-c1">25</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"black"</span>,<span class="pl-s1">bg</span><span class="pl-c1">=</span><span class="pl-s">"deepskyblue"</span>)</td>
        </tr>
        <tr>
          <td id="L683" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="683"></td>
          <td id="LC683" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">heading</span>.<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">10</span>)</td>
        </tr>
        <tr>
          <td id="L684" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="684"></td>
          <td id="LC684" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">style1</span> <span class="pl-c1">=</span> <span class="pl-v">Label</span>(<span class="pl-s1">t</span>,<span class="pl-s1">bg</span><span class="pl-c1">=</span><span class="pl-s">"black"</span>,<span class="pl-s1">height</span><span class="pl-c1">=</span><span class="pl-c1">1</span>,<span class="pl-s1">width</span><span class="pl-c1">=</span><span class="pl-c1">500</span>)</td>
        </tr>
        <tr>
          <td id="L685" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="685"></td>
          <td id="LC685" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">style1</span>.<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">10</span>)</td>
        </tr>
        <tr>
          <td id="L686" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="686"></td>
          <td id="LC686" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">button_dict</span><span class="pl-c1">=</span>{}</td>
        </tr>
        <tr>
          <td id="L687" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="687"></td>
          <td id="LC687" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">with</span> <span class="pl-en">open</span>(<span class="pl-s">"major.json"</span>,<span class="pl-s">'r'</span>) <span class="pl-k">as</span> <span class="pl-s1">file</span>:</td>
        </tr>
        <tr>
          <td id="L688" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="688"></td>
          <td id="LC688" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">a</span><span class="pl-c1">=</span><span class="pl-s1">json</span>.<span class="pl-en">load</span>(<span class="pl-s1">file</span>)</td>
        </tr>
        <tr>
          <td id="L689" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="689"></td>
          <td id="LC689" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">b</span><span class="pl-c1">=</span><span class="pl-c1">0</span></td>
        </tr>
        <tr>
          <td id="L690" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="690"></td>
          <td id="LC690" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-en">list</span>(<span class="pl-s1">a</span>.<span class="pl-en">keys</span>()):</td>
        </tr>
        <tr>
          <td id="L691" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="691"></td>
          <td id="LC691" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>] <span class="pl-c1">=</span> <span class="pl-v">Button</span>(<span class="pl-s1">t</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s1">i</span>, <span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"Black"</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">"verdana"</span>,<span class="pl-c1">16</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">command</span><span class="pl-c1">=</span><span class="pl-en">partial</span>(<span class="pl-s1">majortimes</span>,<span class="pl-s1">b</span>,<span class="pl-s1">i</span>))</td>
        </tr>
        <tr>
          <td id="L692" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="692"></td>
          <td id="LC692" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">button_dict</span>[<span class="pl-s1">i</span>].<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">16</span>)</td>
        </tr>
        <tr>
          <td id="L693" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="693"></td>
          <td id="LC693" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">b</span><span class="pl-c1">=</span><span class="pl-s1">b</span><span class="pl-c1">+</span><span class="pl-c1">1</span></td>
        </tr>
        <tr>
          <td id="L694" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="694"></td>
          <td id="LC694" class="blob-code blob-code-inner js-file-line">
</td>
        </tr>
        <tr>
          <td id="L695" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="695"></td>
          <td id="LC695" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">tamil</span>():</td>
        </tr>
        <tr>
          <td id="L696" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="696"></td>
          <td id="LC696" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">tamils</span><span class="pl-c1">=</span><span class="pl-v">Tk</span>()</td>
        </tr>
        <tr>
          <td id="L697" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="697"></td>
          <td id="LC697" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">tamils</span>.<span class="pl-en">geometry</span>(<span class="pl-s">"1000x2000+10+20"</span>)</td>
        </tr>
        <tr>
          <td id="L698" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="698"></td>
          <td id="LC698" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">tamils</span>.<span class="pl-en">state</span>(<span class="pl-s">"zoomed"</span>)</td>
        </tr>
        <tr>
          <td id="L699" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="699"></td>
          <td id="LC699" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">tamils</span>[<span class="pl-s">'bg'</span>] <span class="pl-c1">=</span> <span class="pl-s">"deepskyblue"</span></td>
        </tr>
        <tr>
          <td id="L700" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="700"></td>
          <td id="LC700" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">heading</span> <span class="pl-c1">=</span> <span class="pl-v">Label</span>(<span class="pl-s1">tamils</span>,<span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s">"Tamil Movies"</span>,<span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">'verdana'</span>,<span class="pl-c1">25</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"black"</span>,<span class="pl-s1">bg</span><span class="pl-c1">=</span><span class="pl-s">"deepskyblue"</span>)</td>
        </tr>
        <tr>
          <td id="L701" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="701"></td>
          <td id="LC701" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">heading</span>.<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">12</span>)</td>
        </tr>
        <tr>
          <td id="L702" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="702"></td>
          <td id="LC702" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">style1</span> <span class="pl-c1">=</span> <span class="pl-v">Label</span>(<span class="pl-s1">tamils</span>,<span class="pl-s1">bg</span><span class="pl-c1">=</span><span class="pl-s">"black"</span>,<span class="pl-s1">height</span><span class="pl-c1">=</span><span class="pl-c1">1</span>,<span class="pl-s1">width</span><span class="pl-c1">=</span><span class="pl-c1">500</span>)</td>
        </tr>
        <tr>
          <td id="L703" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="703"></td>
          <td id="LC703" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">style1</span>.<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">12</span>)</td>
        </tr>
        <tr>
          <td id="L704" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="704"></td>
          <td id="LC704" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">with</span> <span class="pl-en">open</span>(<span class="pl-s">"movies.json"</span>,<span class="pl-s">'r'</span>) <span class="pl-k">as</span> <span class="pl-s1">file</span>:</td>
        </tr>
        <tr>
          <td id="L705" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="705"></td>
          <td id="LC705" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">a</span><span class="pl-c1">=</span><span class="pl-s1">json</span>.<span class="pl-en">load</span>(<span class="pl-s1">file</span>)</td>
        </tr>
        <tr>
          <td id="L706" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="706"></td>
          <td id="LC706" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">tm</span><span class="pl-c1">=</span><span class="pl-s1">a</span>[<span class="pl-s">'Tamil'</span>]</td>
        </tr>
        <tr>
          <td id="L707" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="707"></td>
          <td id="LC707" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">z</span> <span class="pl-c1">=</span> <span class="pl-v">Button</span>(<span class="pl-s1">tamils</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s1">tm</span>[<span class="pl-c1">0</span>], <span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"Black"</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">"verdana"</span>,<span class="pl-c1">18</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">command</span><span class="pl-c1">=</span><span class="pl-en">partial</span>(<span class="pl-s1">tamilmovies</span>,<span class="pl-c1">0</span>,<span class="pl-s1">tm</span>[<span class="pl-c1">0</span>]))</td>
        </tr>
        <tr>
          <td id="L708" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="708"></td>
          <td id="LC708" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">z</span>.<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">18</span>)</td>
        </tr>
        <tr>
          <td id="L709" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="709"></td>
          <td id="LC709" class="blob-code blob-code-inner js-file-line">    </td>
        </tr>
        <tr>
          <td id="L710" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="710"></td>
          <td id="LC710" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">b</span> <span class="pl-c1">=</span> <span class="pl-v">Button</span>(<span class="pl-s1">tamils</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s1">tm</span>[<span class="pl-c1">1</span>], <span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"Black"</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">"verdana"</span>,<span class="pl-c1">18</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">command</span><span class="pl-c1">=</span><span class="pl-en">partial</span>(<span class="pl-s1">tamilmovies</span>,<span class="pl-c1">1</span>,<span class="pl-s1">tm</span>[<span class="pl-c1">1</span>]))</td>
        </tr>
        <tr>
          <td id="L711" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="711"></td>
          <td id="LC711" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">b</span>.<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">18</span>)</td>
        </tr>
        <tr>
          <td id="L712" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="712"></td>
          <td id="LC712" class="blob-code blob-code-inner js-file-line">    </td>
        </tr>
        <tr>
          <td id="L713" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="713"></td>
          <td id="LC713" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">c</span><span class="pl-c1">=</span> <span class="pl-v">Button</span>(<span class="pl-s1">tamils</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s1">tm</span>[<span class="pl-c1">2</span>], <span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"Black"</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">"verdana"</span>,<span class="pl-c1">18</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">command</span><span class="pl-c1">=</span><span class="pl-en">partial</span>(<span class="pl-s1">tamilmovies</span>,<span class="pl-c1">2</span>,<span class="pl-s1">tm</span>[<span class="pl-c1">2</span>]))</td>
        </tr>
        <tr>
          <td id="L714" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="714"></td>
          <td id="LC714" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">c</span>.<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">18</span>)</td>
        </tr>
        <tr>
          <td id="L715" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="715"></td>
          <td id="LC715" class="blob-code blob-code-inner js-file-line">    </td>
        </tr>
        <tr>
          <td id="L716" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="716"></td>
          <td id="LC716" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">d</span><span class="pl-c1">=</span> <span class="pl-v">Button</span>(<span class="pl-s1">tamils</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s1">tm</span>[<span class="pl-c1">3</span>], <span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"Black"</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">"verdana"</span>,<span class="pl-c1">18</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">command</span><span class="pl-c1">=</span><span class="pl-en">partial</span>(<span class="pl-s1">tamilmovies</span>,<span class="pl-c1">3</span>,<span class="pl-s1">tm</span>[<span class="pl-c1">3</span>]))</td>
        </tr>
        <tr>
          <td id="L717" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="717"></td>
          <td id="LC717" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">d</span>.<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">18</span>)</td>
        </tr>
        <tr>
          <td id="L718" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="718"></td>
          <td id="LC718" class="blob-code blob-code-inner js-file-line">    </td>
        </tr>
        <tr>
          <td id="L719" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="719"></td>
          <td id="LC719" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">e</span><span class="pl-c1">=</span> <span class="pl-v">Button</span>(<span class="pl-s1">tamils</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s1">tm</span>[<span class="pl-c1">4</span>], <span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"Black"</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">"verdana"</span>,<span class="pl-c1">18</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">command</span><span class="pl-c1">=</span><span class="pl-en">partial</span>(<span class="pl-s1">tamilmovies</span>,<span class="pl-c1">4</span>,<span class="pl-s1">tm</span>[<span class="pl-c1">4</span>]))</td>
        </tr>
        <tr>
          <td id="L720" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="720"></td>
          <td id="LC720" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">e</span>.<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">18</span>)</td>
        </tr>
        <tr>
          <td id="L721" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="721"></td>
          <td id="LC721" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">tamils</span>.<span class="pl-en">mainloop</span>()</td>
        </tr>
        <tr>
          <td id="L722" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="722"></td>
          <td id="LC722" class="blob-code blob-code-inner js-file-line">    </td>
        </tr>
        <tr>
          <td id="L723" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="723"></td>
          <td id="LC723" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">english</span>():</td>
        </tr>
        <tr>
          <td id="L724" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="724"></td>
          <td id="LC724" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">englishs</span><span class="pl-c1">=</span><span class="pl-v">Tk</span>()</td>
        </tr>
        <tr>
          <td id="L725" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="725"></td>
          <td id="LC725" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">englishs</span>.<span class="pl-en">geometry</span>(<span class="pl-s">"1000x2000+10+20"</span>)</td>
        </tr>
        <tr>
          <td id="L726" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="726"></td>
          <td id="LC726" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">englishs</span>.<span class="pl-en">state</span>(<span class="pl-s">"zoomed"</span>)</td>
        </tr>
        <tr>
          <td id="L727" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="727"></td>
          <td id="LC727" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">englishs</span>[<span class="pl-s">'bg'</span>] <span class="pl-c1">=</span> <span class="pl-s">"deepskyblue"</span></td>
        </tr>
        <tr>
          <td id="L728" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="728"></td>
          <td id="LC728" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">heading</span> <span class="pl-c1">=</span> <span class="pl-v">Label</span>(<span class="pl-s1">englishs</span>,<span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s">"English Movies"</span>,<span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">'verdana'</span>,<span class="pl-c1">25</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"black"</span>,<span class="pl-s1">bg</span><span class="pl-c1">=</span><span class="pl-s">"deepskyblue"</span>)</td>
        </tr>
        <tr>
          <td id="L729" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="729"></td>
          <td id="LC729" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">heading</span>.<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">12</span>)</td>
        </tr>
        <tr>
          <td id="L730" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="730"></td>
          <td id="LC730" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">style1</span> <span class="pl-c1">=</span> <span class="pl-v">Label</span>(<span class="pl-s1">englishs</span>,<span class="pl-s1">bg</span><span class="pl-c1">=</span><span class="pl-s">"black"</span>,<span class="pl-s1">height</span><span class="pl-c1">=</span><span class="pl-c1">1</span>,<span class="pl-s1">width</span><span class="pl-c1">=</span><span class="pl-c1">500</span>)</td>
        </tr>
        <tr>
          <td id="L731" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="731"></td>
          <td id="LC731" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">style1</span>.<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">12</span>)</td>
        </tr>
        <tr>
          <td id="L732" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="732"></td>
          <td id="LC732" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">button_dict</span><span class="pl-c1">=</span>{}</td>
        </tr>
        <tr>
          <td id="L733" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="733"></td>
          <td id="LC733" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">with</span> <span class="pl-en">open</span>(<span class="pl-s">"movies.json"</span>,<span class="pl-s">'r'</span>) <span class="pl-k">as</span> <span class="pl-s1">file</span>:</td>
        </tr>
        <tr>
          <td id="L734" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="734"></td>
          <td id="LC734" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">a</span><span class="pl-c1">=</span><span class="pl-s1">json</span>.<span class="pl-en">load</span>(<span class="pl-s1">file</span>)</td>
        </tr>
        <tr>
          <td id="L735" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="735"></td>
          <td id="LC735" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">tm</span><span class="pl-c1">=</span> <span class="pl-s1">a</span>[<span class="pl-s">'English'</span>]</td>
        </tr>
        <tr>
          <td id="L736" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="736"></td>
          <td id="LC736" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">z</span> <span class="pl-c1">=</span> <span class="pl-v">Button</span>(<span class="pl-s1">englishs</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s1">tm</span>[<span class="pl-c1">0</span>], <span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"Black"</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">"verdana"</span>,<span class="pl-c1">18</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">command</span><span class="pl-c1">=</span><span class="pl-en">partial</span>(<span class="pl-s1">englishmovies</span>,<span class="pl-c1">0</span>,<span class="pl-s1">tm</span>[<span class="pl-c1">0</span>]))</td>
        </tr>
        <tr>
          <td id="L737" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="737"></td>
          <td id="LC737" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">z</span>.<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">18</span>)</td>
        </tr>
        <tr>
          <td id="L738" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="738"></td>
          <td id="LC738" class="blob-code blob-code-inner js-file-line">    </td>
        </tr>
        <tr>
          <td id="L739" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="739"></td>
          <td id="LC739" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">b</span> <span class="pl-c1">=</span> <span class="pl-v">Button</span>(<span class="pl-s1">englishs</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s1">tm</span>[<span class="pl-c1">1</span>], <span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"Black"</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">"verdana"</span>,<span class="pl-c1">18</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">command</span><span class="pl-c1">=</span><span class="pl-en">partial</span>(<span class="pl-s1">englishmovies</span>,<span class="pl-c1">1</span>,<span class="pl-s1">tm</span>[<span class="pl-c1">1</span>]))</td>
        </tr>
        <tr>
          <td id="L740" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="740"></td>
          <td id="LC740" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">b</span>.<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">18</span>)</td>
        </tr>
        <tr>
          <td id="L741" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="741"></td>
          <td id="LC741" class="blob-code blob-code-inner js-file-line">    </td>
        </tr>
        <tr>
          <td id="L742" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="742"></td>
          <td id="LC742" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">c</span><span class="pl-c1">=</span> <span class="pl-v">Button</span>(<span class="pl-s1">englishs</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s1">tm</span>[<span class="pl-c1">2</span>], <span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"Black"</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">"verdana"</span>,<span class="pl-c1">18</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">command</span><span class="pl-c1">=</span><span class="pl-en">partial</span>(<span class="pl-s1">englishmovies</span>,<span class="pl-c1">2</span>,<span class="pl-s1">tm</span>[<span class="pl-c1">2</span>]))</td>
        </tr>
        <tr>
          <td id="L743" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="743"></td>
          <td id="LC743" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">c</span>.<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">18</span>)</td>
        </tr>
        <tr>
          <td id="L744" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="744"></td>
          <td id="LC744" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">englishs</span>.<span class="pl-en">mainloop</span>()</td>
        </tr>
        <tr>
          <td id="L745" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="745"></td>
          <td id="LC745" class="blob-code blob-code-inner js-file-line">        </td>
        </tr>
        <tr>
          <td id="L746" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="746"></td>
          <td id="LC746" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">hindi</span>():</td>
        </tr>
        <tr>
          <td id="L747" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="747"></td>
          <td id="LC747" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">hindis</span><span class="pl-c1">=</span><span class="pl-v">Tk</span>()</td>
        </tr>
        <tr>
          <td id="L748" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="748"></td>
          <td id="LC748" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">hindis</span>.<span class="pl-en">geometry</span>(<span class="pl-s">"1000x2000+10+20"</span>)</td>
        </tr>
        <tr>
          <td id="L749" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="749"></td>
          <td id="LC749" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">hindis</span>.<span class="pl-en">state</span>(<span class="pl-s">"zoomed"</span>)</td>
        </tr>
        <tr>
          <td id="L750" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="750"></td>
          <td id="LC750" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">hindis</span>[<span class="pl-s">'bg'</span>] <span class="pl-c1">=</span> <span class="pl-s">"deepskyblue"</span></td>
        </tr>
        <tr>
          <td id="L751" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="751"></td>
          <td id="LC751" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">heading</span> <span class="pl-c1">=</span> <span class="pl-v">Label</span>(<span class="pl-s1">hindis</span>,<span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s">"Hindi Movies"</span>,<span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">'verdana'</span>,<span class="pl-c1">25</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"black"</span>,<span class="pl-s1">bg</span><span class="pl-c1">=</span><span class="pl-s">"deepskyblue"</span>)</td>
        </tr>
        <tr>
          <td id="L752" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="752"></td>
          <td id="LC752" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">heading</span>.<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">12</span>)</td>
        </tr>
        <tr>
          <td id="L753" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="753"></td>
          <td id="LC753" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">style1</span> <span class="pl-c1">=</span> <span class="pl-v">Label</span>(<span class="pl-s1">hindis</span>,<span class="pl-s1">bg</span><span class="pl-c1">=</span><span class="pl-s">"black"</span>,<span class="pl-s1">height</span><span class="pl-c1">=</span><span class="pl-c1">1</span>,<span class="pl-s1">width</span><span class="pl-c1">=</span><span class="pl-c1">500</span>)</td>
        </tr>
        <tr>
          <td id="L754" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="754"></td>
          <td id="LC754" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">style1</span>.<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">12</span>)</td>
        </tr>
        <tr>
          <td id="L755" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="755"></td>
          <td id="LC755" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">button_dict</span><span class="pl-c1">=</span>{}</td>
        </tr>
        <tr>
          <td id="L756" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="756"></td>
          <td id="LC756" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">with</span> <span class="pl-en">open</span>(<span class="pl-s">"movies.json"</span>,<span class="pl-s">'r'</span>) <span class="pl-k">as</span> <span class="pl-s1">file</span>:</td>
        </tr>
        <tr>
          <td id="L757" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="757"></td>
          <td id="LC757" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">a</span><span class="pl-c1">=</span><span class="pl-s1">json</span>.<span class="pl-en">load</span>(<span class="pl-s1">file</span>)</td>
        </tr>
        <tr>
          <td id="L758" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="758"></td>
          <td id="LC758" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">tm</span><span class="pl-c1">=</span><span class="pl-s1">a</span>[<span class="pl-s">'Hindi'</span>]</td>
        </tr>
        <tr>
          <td id="L759" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="759"></td>
          <td id="LC759" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">z</span> <span class="pl-c1">=</span> <span class="pl-v">Button</span>(<span class="pl-s1">hindis</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s1">tm</span>[<span class="pl-c1">0</span>], <span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"Black"</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">"verdana"</span>,<span class="pl-c1">18</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">command</span><span class="pl-c1">=</span><span class="pl-en">partial</span>(<span class="pl-s1">hindimovies</span>,<span class="pl-c1">0</span>,<span class="pl-s1">tm</span>[<span class="pl-c1">0</span>]))</td>
        </tr>
        <tr>
          <td id="L760" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="760"></td>
          <td id="LC760" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">z</span>.<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">18</span>)</td>
        </tr>
        <tr>
          <td id="L761" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="761"></td>
          <td id="LC761" class="blob-code blob-code-inner js-file-line">    </td>
        </tr>
        <tr>
          <td id="L762" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="762"></td>
          <td id="LC762" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">b</span> <span class="pl-c1">=</span> <span class="pl-v">Button</span>(<span class="pl-s1">hindis</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s1">tm</span>[<span class="pl-c1">1</span>], <span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"Black"</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">"verdana"</span>,<span class="pl-c1">18</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">command</span><span class="pl-c1">=</span><span class="pl-en">partial</span>(<span class="pl-s1">hindimovies</span>,<span class="pl-c1">1</span>,<span class="pl-s1">tm</span>[<span class="pl-c1">1</span>]))</td>
        </tr>
        <tr>
          <td id="L763" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="763"></td>
          <td id="LC763" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">b</span>.<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">18</span>)  </td>
        </tr>
        <tr>
          <td id="L764" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="764"></td>
          <td id="LC764" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">hindis</span>.<span class="pl-en">mainloop</span>()</td>
        </tr>
        <tr>
          <td id="L765" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="765"></td>
          <td id="LC765" class="blob-code blob-code-inner js-file-line">        </td>
        </tr>
        <tr>
          <td id="L766" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="766"></td>
          <td id="LC766" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">telugu</span>():</td>
        </tr>
        <tr>
          <td id="L767" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="767"></td>
          <td id="LC767" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">telugus</span><span class="pl-c1">=</span><span class="pl-v">Tk</span>()</td>
        </tr>
        <tr>
          <td id="L768" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="768"></td>
          <td id="LC768" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">telugus</span>.<span class="pl-en">geometry</span>(<span class="pl-s">"1000x2000+10+20"</span>)</td>
        </tr>
        <tr>
          <td id="L769" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="769"></td>
          <td id="LC769" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">telugus</span>.<span class="pl-en">state</span>(<span class="pl-s">"zoomed"</span>)</td>
        </tr>
        <tr>
          <td id="L770" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="770"></td>
          <td id="LC770" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">telugus</span>[<span class="pl-s">'bg'</span>] <span class="pl-c1">=</span> <span class="pl-s">"deepskyblue"</span></td>
        </tr>
        <tr>
          <td id="L771" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="771"></td>
          <td id="LC771" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">heading</span> <span class="pl-c1">=</span> <span class="pl-v">Label</span>(<span class="pl-s1">telugus</span>,<span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s">"Telugu Movies"</span>,<span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">'verdana'</span>,<span class="pl-c1">25</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"black"</span>,<span class="pl-s1">bg</span><span class="pl-c1">=</span><span class="pl-s">"deepskyblue"</span>)</td>
        </tr>
        <tr>
          <td id="L772" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="772"></td>
          <td id="LC772" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">heading</span>.<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">12</span>)</td>
        </tr>
        <tr>
          <td id="L773" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="773"></td>
          <td id="LC773" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">style1</span> <span class="pl-c1">=</span> <span class="pl-v">Label</span>(<span class="pl-s1">telugus</span>,<span class="pl-s1">bg</span><span class="pl-c1">=</span><span class="pl-s">"black"</span>,<span class="pl-s1">height</span><span class="pl-c1">=</span><span class="pl-c1">1</span>,<span class="pl-s1">width</span><span class="pl-c1">=</span><span class="pl-c1">500</span>)</td>
        </tr>
        <tr>
          <td id="L774" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="774"></td>
          <td id="LC774" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">style1</span>.<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">12</span>)</td>
        </tr>
        <tr>
          <td id="L775" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="775"></td>
          <td id="LC775" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">button_dict</span><span class="pl-c1">=</span>{}</td>
        </tr>
        <tr>
          <td id="L776" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="776"></td>
          <td id="LC776" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">with</span> <span class="pl-en">open</span>(<span class="pl-s">"movies.json"</span>,<span class="pl-s">'r'</span>) <span class="pl-k">as</span> <span class="pl-s1">file</span>:</td>
        </tr>
        <tr>
          <td id="L777" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="777"></td>
          <td id="LC777" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">a</span><span class="pl-c1">=</span><span class="pl-s1">json</span>.<span class="pl-en">load</span>(<span class="pl-s1">file</span>)</td>
        </tr>
        <tr>
          <td id="L778" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="778"></td>
          <td id="LC778" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">tm</span><span class="pl-c1">=</span><span class="pl-s1">a</span>[<span class="pl-s">'Telugu'</span>]</td>
        </tr>
        <tr>
          <td id="L779" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="779"></td>
          <td id="LC779" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">z</span> <span class="pl-c1">=</span> <span class="pl-v">Button</span>(<span class="pl-s1">telugus</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s1">tm</span>[<span class="pl-c1">0</span>], <span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"Black"</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">"verdana"</span>,<span class="pl-c1">18</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">command</span><span class="pl-c1">=</span><span class="pl-en">partial</span>(<span class="pl-s1">telugumovies</span>,<span class="pl-c1">0</span>,<span class="pl-s1">tm</span>[<span class="pl-c1">0</span>]))</td>
        </tr>
        <tr>
          <td id="L780" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="780"></td>
          <td id="LC780" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">z</span>.<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">18</span>)</td>
        </tr>
        <tr>
          <td id="L781" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="781"></td>
          <td id="LC781" class="blob-code blob-code-inner js-file-line">    </td>
        </tr>
        <tr>
          <td id="L782" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="782"></td>
          <td id="LC782" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">b</span> <span class="pl-c1">=</span> <span class="pl-v">Button</span>(<span class="pl-s1">telugus</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s1">tm</span>[<span class="pl-c1">1</span>], <span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"Black"</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">"verdana"</span>,<span class="pl-c1">18</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">command</span><span class="pl-c1">=</span><span class="pl-en">partial</span>(<span class="pl-s1">telugumovies</span>,<span class="pl-c1">1</span>,<span class="pl-s1">tm</span>[<span class="pl-c1">1</span>]))</td>
        </tr>
        <tr>
          <td id="L783" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="783"></td>
          <td id="LC783" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">b</span>.<span class="pl-en">pack</span>(<span class="pl-s1">pady</span><span class="pl-c1">=</span><span class="pl-c1">18</span>)  </td>
        </tr>
        <tr>
          <td id="L784" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="784"></td>
          <td id="LC784" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">telugus</span>.<span class="pl-en">mainloop</span>()</td>
        </tr>
        <tr>
          <td id="L785" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="785"></td>
          <td id="LC785" class="blob-code blob-code-inner js-file-line">        </td>
        </tr>
        <tr>
          <td id="L786" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="786"></td>
          <td id="LC786" class="blob-code blob-code-inner js-file-line">
</td>
        </tr>
        <tr>
          <td id="L787" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="787"></td>
          <td id="LC787" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">language</span>():</td>
        </tr>
        <tr>
          <td id="L788" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="788"></td>
          <td id="LC788" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">root</span><span class="pl-c1">=</span><span class="pl-v">Tk</span>()</td>
        </tr>
        <tr>
          <td id="L789" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="789"></td>
          <td id="LC789" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">root</span>.<span class="pl-en">geometry</span>(<span class="pl-s">'1000x2000+10+20'</span>)</td>
        </tr>
        <tr>
          <td id="L790" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="790"></td>
          <td id="LC790" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">root</span>.<span class="pl-en">state</span>(<span class="pl-s">'zoomed'</span>)</td>
        </tr>
        <tr>
          <td id="L791" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="791"></td>
          <td id="LC791" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">root</span>.<span class="pl-en">title</span>(<span class="pl-s">'BookyMyShow'</span>)</td>
        </tr>
        <tr>
          <td id="L792" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="792"></td>
          <td id="LC792" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">root</span>[<span class="pl-s">'bg'</span>] <span class="pl-c1">=</span> <span class="pl-s">"deepskyblue"</span></td>
        </tr>
        <tr>
          <td id="L793" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="793"></td>
          <td id="LC793" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">heading</span> <span class="pl-c1">=</span> <span class="pl-v">Label</span>(<span class="pl-s1">root</span>,<span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s">"BookMyShow - Entertainment Ki Nayi Bhasha"</span>,<span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">'verdana'</span>,<span class="pl-c1">25</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"black"</span>,<span class="pl-s1">bg</span><span class="pl-c1">=</span><span class="pl-s">"deepskyblue"</span>)</td>
        </tr>
        <tr>
          <td id="L794" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="794"></td>
          <td id="LC794" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">heading</span>.<span class="pl-en">place</span>(<span class="pl-s1">x</span><span class="pl-c1">=</span><span class="pl-c1">400</span>,<span class="pl-s1">y</span><span class="pl-c1">=</span><span class="pl-c1">5</span>)</td>
        </tr>
        <tr>
          <td id="L795" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="795"></td>
          <td id="LC795" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">style1</span> <span class="pl-c1">=</span> <span class="pl-v">Label</span>(<span class="pl-s1">root</span>,<span class="pl-s1">bg</span><span class="pl-c1">=</span><span class="pl-s">"black"</span>,<span class="pl-s1">height</span><span class="pl-c1">=</span><span class="pl-c1">1</span>,<span class="pl-s1">width</span><span class="pl-c1">=</span><span class="pl-c1">500</span>)</td>
        </tr>
        <tr>
          <td id="L796" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="796"></td>
          <td id="LC796" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">style1</span>.<span class="pl-en">place</span>(<span class="pl-s1">x</span><span class="pl-c1">=</span><span class="pl-c1">0</span>,<span class="pl-s1">y</span><span class="pl-c1">=</span><span class="pl-c1">50</span>)</td>
        </tr>
        <tr>
          <td id="L797" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="797"></td>
          <td id="LC797" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">date</span> <span class="pl-c1">=</span> <span class="pl-v">Label</span>(<span class="pl-s1">root</span>,<span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s1">datetime</span>.<span class="pl-en">now</span>(),<span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">'verdana'</span>,<span class="pl-c1">10</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">bg</span><span class="pl-c1">=</span><span class="pl-s">"deepskyblue"</span>)</td>
        </tr>
        <tr>
          <td id="L798" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="798"></td>
          <td id="LC798" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">date</span>.<span class="pl-en">place</span>(<span class="pl-s1">x</span><span class="pl-c1">=</span><span class="pl-c1">640</span>,<span class="pl-s1">y</span><span class="pl-c1">=</span><span class="pl-c1">50</span>)</td>
        </tr>
        <tr>
          <td id="L799" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="799"></td>
          <td id="LC799" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">frame1</span> <span class="pl-c1">=</span> <span class="pl-v">LabelFrame</span>(<span class="pl-s1">root</span>,<span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s">" Movie Language"</span>,<span class="pl-s1">width</span><span class="pl-c1">=</span><span class="pl-c1">425</span>,<span class="pl-s1">height</span><span class="pl-c1">=</span><span class="pl-c1">425</span>,<span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">'verdana'</span>,<span class="pl-c1">30</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">borderwidth</span><span class="pl-c1">=</span><span class="pl-c1">3</span>,<span class="pl-s1">relief</span><span class="pl-c1">=</span><span class="pl-v">RIDGE</span>,<span class="pl-s1">highlightthickness</span><span class="pl-c1">=</span><span class="pl-c1">4</span>,<span class="pl-s1">bg</span><span class="pl-c1">=</span><span class="pl-s">"deepskyblue"</span>,<span class="pl-s1">highlightcolor</span><span class="pl-c1">=</span><span class="pl-s">"deepskyblue"</span>,<span class="pl-s1">highlightbackground</span><span class="pl-c1">=</span><span class="pl-s">"deepskyblue"</span>,<span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"black"</span>)</td>
        </tr>
        <tr>
          <td id="L800" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="800"></td>
          <td id="LC800" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">frame1</span>.<span class="pl-en">place</span>(<span class="pl-s1">x</span><span class="pl-c1">=</span><span class="pl-c1">500</span>,<span class="pl-s1">y</span><span class="pl-c1">=</span><span class="pl-c1">90</span>)</td>
        </tr>
        <tr>
          <td id="L801" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="801"></td>
          <td id="LC801" class="blob-code blob-code-inner js-file-line">            </td>
        </tr>
        <tr>
          <td id="L802" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="802"></td>
          <td id="LC802" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">tamilm</span> <span class="pl-c1">=</span> <span class="pl-v">Button</span>(<span class="pl-s1">root</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s">"Tamil"</span>, <span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"Black"</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">"verdana"</span>,<span class="pl-c1">18</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">command</span><span class="pl-c1">=</span><span class="pl-s1">tamil</span>)</td>
        </tr>
        <tr>
          <td id="L803" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="803"></td>
          <td id="LC803" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">tamilm</span>.<span class="pl-en">place</span>(<span class="pl-s1">x</span><span class="pl-c1">=</span><span class="pl-c1">670</span>,<span class="pl-s1">y</span><span class="pl-c1">=</span><span class="pl-c1">170</span>)  </td>
        </tr>
        <tr>
          <td id="L804" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="804"></td>
          <td id="LC804" class="blob-code blob-code-inner js-file-line">
</td>
        </tr>
        <tr>
          <td id="L805" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="805"></td>
          <td id="LC805" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">hindim</span> <span class="pl-c1">=</span> <span class="pl-v">Button</span>(<span class="pl-s1">root</span>,<span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s">"Hindi"</span>,<span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">'verdana'</span>,<span class="pl-c1">18</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">command</span><span class="pl-c1">=</span><span class="pl-s1">hindi</span>)</td>
        </tr>
        <tr>
          <td id="L806" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="806"></td>
          <td id="LC806" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">hindim</span>.<span class="pl-en">place</span>(<span class="pl-s1">x</span><span class="pl-c1">=</span><span class="pl-c1">670</span>,<span class="pl-s1">y</span><span class="pl-c1">=</span><span class="pl-c1">250</span>)</td>
        </tr>
        <tr>
          <td id="L807" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="807"></td>
          <td id="LC807" class="blob-code blob-code-inner js-file-line">
</td>
        </tr>
        <tr>
          <td id="L808" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="808"></td>
          <td id="LC808" class="blob-code blob-code-inner js-file-line">
</td>
        </tr>
        <tr>
          <td id="L809" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="809"></td>
          <td id="LC809" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">englishm</span> <span class="pl-c1">=</span> <span class="pl-v">Button</span>(<span class="pl-s1">root</span>,<span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s">"English"</span>,<span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">'verdana'</span>,<span class="pl-c1">18</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">command</span><span class="pl-c1">=</span><span class="pl-s1">english</span>)</td>
        </tr>
        <tr>
          <td id="L810" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="810"></td>
          <td id="LC810" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">englishm</span>.<span class="pl-en">place</span>(<span class="pl-s1">x</span><span class="pl-c1">=</span><span class="pl-c1">660</span>,<span class="pl-s1">y</span><span class="pl-c1">=</span><span class="pl-c1">330</span>)</td>
        </tr>
        <tr>
          <td id="L811" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="811"></td>
          <td id="LC811" class="blob-code blob-code-inner js-file-line">            </td>
        </tr>
        <tr>
          <td id="L812" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="812"></td>
          <td id="LC812" class="blob-code blob-code-inner js-file-line">
</td>
        </tr>
        <tr>
          <td id="L813" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="813"></td>
          <td id="LC813" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">telugum</span> <span class="pl-c1">=</span> <span class="pl-v">Button</span>(<span class="pl-s1">root</span>,<span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s">"Telugu"</span>,<span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">'verdana'</span>,<span class="pl-c1">18</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">command</span><span class="pl-c1">=</span><span class="pl-s1">telugu</span>)</td>
        </tr>
        <tr>
          <td id="L814" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="814"></td>
          <td id="LC814" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">telugum</span>.<span class="pl-en">place</span>(<span class="pl-s1">x</span><span class="pl-c1">=</span><span class="pl-c1">660</span>,<span class="pl-s1">y</span><span class="pl-c1">=</span><span class="pl-c1">410</span>)</td>
        </tr>
        <tr>
          <td id="L815" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="815"></td>
          <td id="LC815" class="blob-code blob-code-inner js-file-line">            </td>
        </tr>
        <tr>
          <td id="L816" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="816"></td>
          <td id="LC816" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">root</span>.<span class="pl-en">mainloop</span>()</td>
        </tr>
        <tr>
          <td id="L817" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="817"></td>
          <td id="LC817" class="blob-code blob-code-inner js-file-line">
</td>
        </tr>
        <tr>
          <td id="L818" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="818"></td>
          <td id="LC818" class="blob-code blob-code-inner js-file-line">    </td>
        </tr>
        <tr>
          <td id="L819" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="819"></td>
          <td id="LC819" class="blob-code blob-code-inner js-file-line">
</td>
        </tr>
        <tr>
          <td id="L820" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="820"></td>
          <td id="LC820" class="blob-code blob-code-inner js-file-line"><span class="pl-s1">ws</span> <span class="pl-c1">=</span> <span class="pl-v">Tk</span>()</td>
        </tr>
        <tr>
          <td id="L821" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="821"></td>
          <td id="LC821" class="blob-code blob-code-inner js-file-line"><span class="pl-s1">ws</span>.<span class="pl-en">title</span>(<span class="pl-s">"window"</span>)</td>
        </tr>
        <tr>
          <td id="L822" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="822"></td>
          <td id="LC822" class="blob-code blob-code-inner js-file-line">
</td>
        </tr>
        <tr>
          <td id="L823" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="823"></td>
          <td id="LC823" class="blob-code blob-code-inner js-file-line"><span class="pl-s1">width</span><span class="pl-c1">=</span> <span class="pl-s1">ws</span>.<span class="pl-en">winfo_screenwidth</span>()</td>
        </tr>
        <tr>
          <td id="L824" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="824"></td>
          <td id="LC824" class="blob-code blob-code-inner js-file-line"><span class="pl-s1">height</span><span class="pl-c1">=</span> <span class="pl-s1">ws</span>.<span class="pl-en">winfo_screenheight</span>()</td>
        </tr>
        <tr>
          <td id="L825" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="825"></td>
          <td id="LC825" class="blob-code blob-code-inner js-file-line">
</td>
        </tr>
        <tr>
          <td id="L826" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="826"></td>
          <td id="LC826" class="blob-code blob-code-inner js-file-line"><span class="pl-s1">ws</span>.<span class="pl-en">geometry</span>(<span class="pl-s">"%dx%d"</span> <span class="pl-c1">%</span> (<span class="pl-s1">width</span>, <span class="pl-s1">height</span>))</td>
        </tr>
        <tr>
          <td id="L827" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="827"></td>
          <td id="LC827" class="blob-code blob-code-inner js-file-line"><span class="pl-s1">ws</span>.<span class="pl-en">title</span>(<span class="pl-s">'BookMyShow Login Page'</span>)</td>
        </tr>
        <tr>
          <td id="L828" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="828"></td>
          <td id="LC828" class="blob-code blob-code-inner js-file-line"><span class="pl-s1">ws</span>.<span class="pl-en">resizable</span>(<span class="pl-c1">False</span>, <span class="pl-c1">False</span>)</td>
        </tr>
        <tr>
          <td id="L829" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="829"></td>
          <td id="LC829" class="blob-code blob-code-inner js-file-line">
</td>
        </tr>
        <tr>
          <td id="L830" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="830"></td>
          <td id="LC830" class="blob-code blob-code-inner js-file-line"><span class="pl-s1">imgTemp</span> <span class="pl-c1">=</span> <span class="pl-v">Image</span>.<span class="pl-en">open</span>(<span class="pl-s">"movies.jpg"</span>)</td>
        </tr>
        <tr>
          <td id="L831" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="831"></td>
          <td id="LC831" class="blob-code blob-code-inner js-file-line"><span class="pl-s1">img2</span> <span class="pl-c1">=</span> <span class="pl-s1">imgTemp</span>.<span class="pl-en">resize</span>((<span class="pl-s1">width</span>,<span class="pl-s1">height</span>))</td>
        </tr>
        <tr>
          <td id="L832" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="832"></td>
          <td id="LC832" class="blob-code blob-code-inner js-file-line"><span class="pl-s1">img</span> <span class="pl-c1">=</span> <span class="pl-v">ImageTk</span>.<span class="pl-v">PhotoImage</span>(<span class="pl-s1">img2</span>)</td>
        </tr>
        <tr>
          <td id="L833" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="833"></td>
          <td id="LC833" class="blob-code blob-code-inner js-file-line">
</td>
        </tr>
        <tr>
          <td id="L834" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="834"></td>
          <td id="LC834" class="blob-code blob-code-inner js-file-line"><span class="pl-s1">label</span> <span class="pl-c1">=</span> <span class="pl-v">Label</span>(<span class="pl-s1">ws</span>,<span class="pl-s1">image</span><span class="pl-c1">=</span><span class="pl-s1">img</span>)</td>
        </tr>
        <tr>
          <td id="L835" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="835"></td>
          <td id="LC835" class="blob-code blob-code-inner js-file-line"><span class="pl-s1">label</span>.<span class="pl-en">pack</span>(<span class="pl-s1">side</span><span class="pl-c1">=</span><span class="pl-s">'top'</span>,<span class="pl-s1">fill</span><span class="pl-c1">=</span><span class="pl-v">Y</span>,<span class="pl-s1">expand</span><span class="pl-c1">=</span><span class="pl-c1">True</span>)</td>
        </tr>
        <tr>
          <td id="L836" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="836"></td>
          <td id="LC836" class="blob-code blob-code-inner js-file-line"><span class="pl-s1">heading</span> <span class="pl-c1">=</span> <span class="pl-v">Label</span>(<span class="pl-s1">ws</span>,<span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s">"Login Page"</span>,<span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">'verdana'</span>,<span class="pl-c1">30</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"black"</span>,<span class="pl-s1">bg</span><span class="pl-c1">=</span><span class="pl-s">"white"</span>)</td>
        </tr>
        <tr>
          <td id="L837" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="837"></td>
          <td id="LC837" class="blob-code blob-code-inner js-file-line"><span class="pl-s1">heading</span>.<span class="pl-en">place</span>(<span class="pl-s1">x</span><span class="pl-c1">=</span><span class="pl-c1">600</span>,<span class="pl-s1">y</span><span class="pl-c1">=</span><span class="pl-c1">50</span>)</td>
        </tr>
        <tr>
          <td id="L838" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="838"></td>
          <td id="LC838" class="blob-code blob-code-inner js-file-line"><span class="pl-s1">label1_tk</span> <span class="pl-c1">=</span> <span class="pl-v">Label</span>(<span class="pl-s1">ws</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s">"Name"</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">'arial'</span>,<span class="pl-c1">30</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"black"</span>,<span class="pl-s1">bg</span><span class="pl-c1">=</span><span class="pl-s">"white"</span>)</td>
        </tr>
        <tr>
          <td id="L839" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="839"></td>
          <td id="LC839" class="blob-code blob-code-inner js-file-line"><span class="pl-s1">label1_tk</span>.<span class="pl-en">place</span>(<span class="pl-s1">x</span><span class="pl-c1">=</span><span class="pl-c1">650</span>,<span class="pl-s1">y</span><span class="pl-c1">=</span><span class="pl-c1">150</span>)</td>
        </tr>
        <tr>
          <td id="L840" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="840"></td>
          <td id="LC840" class="blob-code blob-code-inner js-file-line">
</td>
        </tr>
        <tr>
          <td id="L841" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="841"></td>
          <td id="LC841" class="blob-code blob-code-inner js-file-line"><span class="pl-s1">entry1_tk</span> <span class="pl-c1">=</span> <span class="pl-v">Entry</span>(<span class="pl-s1">ws</span>, <span class="pl-s1">bd</span> <span class="pl-c1">=</span> <span class="pl-c1">9</span>,<span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"black"</span>)</td>
        </tr>
        <tr>
          <td id="L842" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="842"></td>
          <td id="LC842" class="blob-code blob-code-inner js-file-line"><span class="pl-s1">entry1_tk</span>.<span class="pl-en">place</span>(<span class="pl-s1">x</span><span class="pl-c1">=</span><span class="pl-c1">650</span>,<span class="pl-s1">y</span><span class="pl-c1">=</span><span class="pl-c1">230</span>)</td>
        </tr>
        <tr>
          <td id="L843" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="843"></td>
          <td id="LC843" class="blob-code blob-code-inner js-file-line">
</td>
        </tr>
        <tr>
          <td id="L844" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="844"></td>
          <td id="LC844" class="blob-code blob-code-inner js-file-line"><span class="pl-s1">label1_tk</span> <span class="pl-c1">=</span> <span class="pl-v">Label</span>(<span class="pl-s1">ws</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s">"Password"</span>,<span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">'arial'</span>,<span class="pl-c1">30</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"black"</span>,<span class="pl-s1">bg</span><span class="pl-c1">=</span><span class="pl-s">"white"</span>)</td>
        </tr>
        <tr>
          <td id="L845" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="845"></td>
          <td id="LC845" class="blob-code blob-code-inner js-file-line"><span class="pl-s1">label1_tk</span>.<span class="pl-en">place</span>(<span class="pl-s1">x</span><span class="pl-c1">=</span><span class="pl-c1">625</span>,<span class="pl-s1">y</span><span class="pl-c1">=</span><span class="pl-c1">300</span>)</td>
        </tr>
        <tr>
          <td id="L846" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="846"></td>
          <td id="LC846" class="blob-code blob-code-inner js-file-line">
</td>
        </tr>
        <tr>
          <td id="L847" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="847"></td>
          <td id="LC847" class="blob-code blob-code-inner js-file-line"><span class="pl-s1">entry2_tk</span> <span class="pl-c1">=</span> <span class="pl-v">Entry</span>(<span class="pl-s1">ws</span>, <span class="pl-s1">bd</span> <span class="pl-c1">=</span> <span class="pl-c1">9</span>, <span class="pl-s1">show</span><span class="pl-c1">=</span><span class="pl-s">"*"</span>)</td>
        </tr>
        <tr>
          <td id="L848" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="848"></td>
          <td id="LC848" class="blob-code blob-code-inner js-file-line"><span class="pl-s1">entry2_tk</span>.<span class="pl-en">place</span>(<span class="pl-s1">x</span><span class="pl-c1">=</span><span class="pl-c1">650</span>,<span class="pl-s1">y</span><span class="pl-c1">=</span><span class="pl-c1">380</span>)</td>
        </tr>
        <tr>
          <td id="L849" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="849"></td>
          <td id="LC849" class="blob-code blob-code-inner js-file-line">
</td>
        </tr>
        <tr>
          <td id="L850" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="850"></td>
          <td id="LC850" class="blob-code blob-code-inner js-file-line"><span class="pl-s1">loginButton</span> <span class="pl-c1">=</span> <span class="pl-v">Button</span>(<span class="pl-s1">ws</span>, <span class="pl-s1">text</span><span class="pl-c1">=</span><span class="pl-s">"Login"</span>, <span class="pl-s1">bd</span><span class="pl-c1">=</span><span class="pl-c1">5</span>, <span class="pl-s1">font</span><span class="pl-c1">=</span>(<span class="pl-s">'arial'</span>,<span class="pl-c1">25</span>,<span class="pl-s">'bold'</span>),<span class="pl-s1">fg</span><span class="pl-c1">=</span><span class="pl-s">"white"</span>,<span class="pl-s1">bg</span><span class="pl-c1">=</span><span class="pl-s">"black"</span>,<span class="pl-s1">command</span><span class="pl-c1">=</span><span class="pl-s1">language</span>)</td>
        </tr>
        <tr>
          <td id="L851" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="851"></td>
          <td id="LC851" class="blob-code blob-code-inner js-file-line"><span class="pl-s1">loginButton</span>.<span class="pl-en">place</span>(<span class="pl-s1">x</span><span class="pl-c1">=</span><span class="pl-c1">660</span>,<span class="pl-s1">y</span><span class="pl-c1">=</span><span class="pl-c1">450</span>)</td>
        </tr>
        <tr>
          <td id="L852" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="852"></td>
          <td id="LC852" class="blob-code blob-code-inner js-file-line"><span class="pl-s1">ws</span>.<span class="pl-en">mainloop</span>()</td>
        </tr>
        <tr>
          <td id="L853" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="853"></td>
          <td id="LC853" class="blob-code blob-code-inner js-file-line">
</td>
        </tr>
        <tr>
          <td id="L854" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="854"></td>
          <td id="LC854" class="blob-code blob-code-inner js-file-line">
</td>
        </tr>
        <tr>
          <td id="L855" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="855"></td>
          <td id="LC855" class="blob-code blob-code-inner js-file-line">            </td>
        </tr>
        <tr>
          <td id="L856" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="856"></td>
          <td id="LC856" class="blob-code blob-code-inner js-file-line">    </td>
        </tr>
        <tr>
          <td id="L857" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="857"></td>
          <td id="LC857" class="blob-code blob-code-inner js-file-line">
</td>
        </tr>
        <tr>
          <td id="L858" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="858"></td>
          <td id="LC858" class="blob-code blob-code-inner js-file-line">            </td>
        </tr>
        <tr>
          <td id="L859" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="859"></td>
          <td id="LC859" class="blob-code blob-code-inner js-file-line">    </td>
        </tr>
        <tr>
          <td id="L860" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="860"></td>
          <td id="LC860" class="blob-code blob-code-inner js-file-line">    </td>
        </tr>
  </tbody></table>
</div>

  <details class="details-reset details-overlay BlobToolbar position-absolute js-file-line-actions dropdown d-none" aria-hidden="true">
    <summary class="btn-octicon ml-0 px-2 p-0 color-bg-default border color-border-default rounded-2" aria-label="Inline file action toolbar" aria-haspopup="menu" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-kebab-horizontal">
    <path d="M8 9a1.5 1.5 0 100-3 1.5 1.5 0 000 3zM1.5 9a1.5 1.5 0 100-3 1.5 1.5 0 000 3zm13 0a1.5 1.5 0 100-3 1.5 1.5 0 000 3z"></path>
</svg>
    </summary>
    <details-menu role="menu" data-focus-trap="active"><span class="sentinel" tabindex="0" aria-hidden="true"></span>

      <ul class="BlobToolbar-dropdown dropdown-menu dropdown-menu-se ml-2 mt-2" style="width:185px">
        <li>
          <clipboard-copy role="menuitem" class="dropdown-item" id="js-copy-lines" style="cursor:pointer;" aria-label="Copy lines" tabindex="0">
            Copy lines
          </clipboard-copy>
        </li>
        <li>
          <clipboard-copy role="menuitem" class="dropdown-item" id="js-copy-permalink" style="cursor:pointer;" aria-label="Copy permalink" tabindex="0">
            Copy permalink
          </clipboard-copy>
        </li>
        <li><a class="dropdown-item js-update-url-with-hash" id="js-view-git-blame" role="menuitem" href="https://github.com/reyashv/python/blame/6896039a3a2afc5582fe93390554dd72d0023ef8/tkinterproject.py">View git blame</a></li>
          <li><a class="dropdown-item" id="js-new-issue" role="menuitem" href="https://github.com/reyashv/python/issues/new">Reference in new issue</a></li>
      </ul>
    <span class="sentinel" tabindex="0" aria-hidden="true"></span></details-menu>
  </details>

    </div>

    </div>


  

  <details class="details-reset details-overlay details-overlay-dark" id="jumpto-line-details-dialog">
    <summary data-hotkey="l" aria-label="Jump to line" role="button"></summary>
    <details-dialog class="Box Box--overlay d-flex flex-column anim-fade-in fast linejump overflow-hidden" aria-label="Jump to line" role="dialog" aria-modal="true">
      <!-- '"` --><!-- </textarea></xmp> --><form class="js-jump-to-line-form Box-body d-flex" data-turbo="false" action="https://github.com/reyashv/python/blob/main/tkinterproject.py" accept-charset="UTF-8" method="get">
        <input class="form-control flex-auto mr-3 linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line…" aria-label="Jump to line" autofocus="">
          <button data-close-dialog="" type="submit" data-view-component="true" class="btn">    Go
</button>
</form>    </details-dialog>
  </details>

    <div class="Popover anim-scale-in js-tagsearch-popover" hidden="" data-tagsearch-url="/reyashv/python/find-definition" data-tagsearch-ref="main" data-tagsearch-code-nav-context="BLOB_VIEW">
  <div class="Popover-message Popover-message--large Popover-message--top-left TagsearchPopover mt-1 mb-4 mx-auto Box color-shadow-large">
    <div class="TagsearchPopover-content js-tagsearch-popover-content overflow-auto" style="will-change:transform;">
    </div>
  </div>
</div>



    <div class="pt-3">
      <details class="details-reset details-overlay details-overlay-dark ">
                <summary data-view-component="true" class="btn-link" role="button">    Give feedback
</summary>

  <details-dialog class="Box d-flex flex-column anim-fade-in fast Box--overlay overflow-visible" aria-label="Provide feedback" src="/reyashv/python/repos/code_nav_survey" role="dialog" aria-modal="true">
    <div class="Box-header">
      <button class="Box-btn-octicon btn-octicon float-right" type="button" aria-label="Close dialog" data-close-dialog="">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path fill-rule="evenodd" d="M3.72 3.72a.75.75 0 011.06 0L8 6.94l3.22-3.22a.75.75 0 111.06 1.06L9.06 8l3.22 3.22a.75.75 0 11-1.06 1.06L8 9.06l-3.22 3.22a.75.75 0 01-1.06-1.06L6.94 8 3.72 4.78a.75.75 0 010-1.06z"></path>
</svg>
      </button>
        <h1 class="Box-title">Provide feedback</h1>
    </div>
      <div class="Box-body overflow-auto">
                  <include-fragment>
            <svg style="box-sizing: content-box; color: var(--color-icon-primary);" width="32" height="32" viewBox="0 0 16 16" fill="none" data-view-component="true" class="my-3 mx-auto d-block anim-rotate">
  <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke"></circle>
  <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke"></path>
</svg>
          </include-fragment>

      </div>
  </details-dialog>
</details>
    </div>
</div>

  </div>

  </turbo-frame>


    </main>
  </div>

  </div>

          <footer class="footer width-full container-xl p-responsive">
  <h2 class="sr-only">Footer</h2>

  <div class="position-relative d-flex flex-items-center pb-2 f6 color-fg-muted border-top color-border-muted flex-column-reverse flex-lg-row flex-wrap flex-lg-nowrap mt-6 pt-6">
    <div class="list-style-none d-flex flex-wrap col-0 col-lg-2 flex-justify-start flex-lg-justify-between mb-2 mb-lg-0">
      <div class="mt-2 mt-lg-0 d-flex flex-items-center">
        <a aria-label="Homepage" title="GitHub" class="footer-octicon mr-2" href="https://github.com/">
          <svg aria-hidden="true" height="24" viewBox="0 0 16 16" version="1.1" width="24" data-view-component="true" class="octicon octicon-mark-github">
    <path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"></path>
</svg>
</a>        <span>
        © 2023 GitHub, Inc.
        </span>
      </div>
    </div>

    <nav aria-label="footer" class="col-12 col-lg-8">
      <h3 class="sr-only" id="sr-footer-heading">Footer navigation</h3>
      <ul class="list-style-none d-flex flex-wrap col-12 flex-justify-center flex-lg-justify-between mb-2 mb-lg-0" aria-labelledby="sr-footer-heading">
          <li class="mr-3 mr-lg-0"><a href="https://docs.github.com/site-policy/github-terms/github-terms-of-service" data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to terms&quot;,&quot;label&quot;:&quot;text:terms&quot;}">Terms</a></li>
          <li class="mr-3 mr-lg-0"><a href="https://docs.github.com/site-policy/privacy-policies/github-privacy-statement" data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to privacy&quot;,&quot;label&quot;:&quot;text:privacy&quot;}">Privacy</a></li>
          <li class="mr-3 mr-lg-0"><a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to security&quot;,&quot;label&quot;:&quot;text:security&quot;}" href="https://github.com/security">Security</a></li>
          <li class="mr-3 mr-lg-0"><a href="https://www.githubstatus.com/" data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to status&quot;,&quot;label&quot;:&quot;text:status&quot;}">Status</a></li>
          <li class="mr-3 mr-lg-0"><a data-ga-click="Footer, go to help, text:Docs" href="https://docs.github.com/">Docs</a></li>
          <li class="mr-3 mr-lg-0"><a href="https://support.github.com/?tags=dotcom-footer" data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to contact&quot;,&quot;label&quot;:&quot;text:contact&quot;}">Contact GitHub</a></li>
          <li class="mr-3 mr-lg-0"><a href="https://github.com/pricing" data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to Pricing&quot;,&quot;label&quot;:&quot;text:Pricing&quot;}">Pricing</a></li>
        <li class="mr-3 mr-lg-0"><a href="https://docs.github.com/" data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to api&quot;,&quot;label&quot;:&quot;text:api&quot;}">API</a></li>
        <li class="mr-3 mr-lg-0"><a href="https://services.github.com/" data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to training&quot;,&quot;label&quot;:&quot;text:training&quot;}">Training</a></li>
          <li class="mr-3 mr-lg-0"><a href="https://github.blog/" data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to blog&quot;,&quot;label&quot;:&quot;text:blog&quot;}">Blog</a></li>
          <li><a data-ga-click="Footer, go to about, text:about" href="https://github.com/about">About</a></li>
      </ul>
    </nav>
  </div>

  <div class="d-flex flex-justify-center pb-6">
    <span class="f6 color-fg-muted"></span>
  </div>
</footer>




  <div id="ajax-error-message" class="ajax-error-message flash flash-error" hidden="">
    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert">
    <path fill-rule="evenodd" d="M8.22 1.754a.25.25 0 00-.44 0L1.698 13.132a.25.25 0 00.22.368h12.164a.25.25 0 00.22-.368L8.22 1.754zm-1.763-.707c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0114.082 15H1.918a1.75 1.75 0 01-1.543-2.575L6.457 1.047zM9 11a1 1 0 11-2 0 1 1 0 012 0zm-.25-5.25a.75.75 0 00-1.5 0v2.5a.75.75 0 001.5 0v-2.5z"></path>
</svg>
    <button type="button" class="flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path fill-rule="evenodd" d="M3.72 3.72a.75.75 0 011.06 0L8 6.94l3.22-3.22a.75.75 0 111.06 1.06L9.06 8l3.22 3.22a.75.75 0 11-1.06 1.06L8 9.06l-3.22 3.22a.75.75 0 01-1.06-1.06L6.94 8 3.72 4.78a.75.75 0 010-1.06z"></path>
</svg>
    </button>
    You can’t perform that action at this time.
  </div>

  <div class="js-stale-session-flash flash flash-warn flash-banner" hidden="">
    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert">
    <path fill-rule="evenodd" d="M8.22 1.754a.25.25 0 00-.44 0L1.698 13.132a.25.25 0 00.22.368h12.164a.25.25 0 00.22-.368L8.22 1.754zm-1.763-.707c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0114.082 15H1.918a1.75 1.75 0 01-1.543-2.575L6.457 1.047zM9 11a1 1 0 11-2 0 1 1 0 012 0zm-.25-5.25a.75.75 0 00-1.5 0v2.5a.75.75 0 001.5 0v-2.5z"></path>
</svg>
    <span class="js-stale-session-flash-signed-in" hidden="">You signed in with another tab or window. <a href="https://github.com/reyashv/python/blob/main/tkinterproject.py">Reload</a> to refresh your session.</span>
    <span class="js-stale-session-flash-signed-out" hidden="">You signed out in another tab or window. <a href="https://github.com/reyashv/python/blob/main/tkinterproject.py">Reload</a> to refresh your session.</span>
  </div>
    <template id="site-details-dialog"></template>

    <div class="Popover js-hovercard-content position-absolute" style="display: none; outline: none;" tabindex="0">
  <div class="Popover-message Popover-message--bottom-left Popover-message--large Box color-shadow-large" style="width:360px;"></div>
</div>

    <template id="snippet-clipboard-copy-button"></template>


    <style>
      .user-mention[href$="/samyuktaakannan"] {
        color: var(--color-user-mention-fg);
        background-color: var(--color-user-mention-bg);
        border-radius: 2px;
        margin-left: -2px;
        margin-right: -2px;
        padding: 0 2px;
      }
    </style>


    </div>

    <div id="js-global-screen-reader-notice" class="sr-only" aria-live="polite">python/tkinterproject.py at main · reyashv/python</div>
  


</body></html>