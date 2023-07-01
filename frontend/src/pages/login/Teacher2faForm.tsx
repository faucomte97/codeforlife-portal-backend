import React from 'react';

import { paths } from '../../app/routes';
import BaseForm from './BaseForm';
import { SubmitButton, TextField } from 'codeforlife/lib/esm/components/form';
import * as Yup from 'yup';
import { Button, Stack } from '@mui/material';

interface Login2faFormValues {
  token: string;
}

const initialValues: Login2faFormValues = {
  token: ''
};

const Teacher2faForm: React.FC = () => {
  return (
    <BaseForm
      themedBoxProps={{ userType: 'teacher' }}
      header='Welcome'
      subheader='Please enter the token generated by your token generator.'
      initialValues={initialValues}
      onSubmit={(values, { setSubmitting }) => {
        // TODO: Connect this to the backend
        console.log(values);
        setSubmitting(false);
      }}
    >
      <TextField
        name="token"
        helperText="Enter your code from your app"
        validate={Yup
          .string()
          .matches(/^[0-9]{6}$/, 'Invalid token')}
        required
      />
      <Button
        className='body'
        href={paths.login.teacher.backupToken._}
      >
        Use a backup token
      </Button>
      <Stack direction="row" spacing={2} justifyContent="space-between">
        <Button
          href={paths.login.teacher._}
          variant='outlined'
        >
          Cancel
        </Button>
        <SubmitButton
          // TODO: Remove href and replace with submit functionality
          href={paths.teacher.dashboard.school._} />
      </Stack>
    </BaseForm>
  );
};

export default Teacher2faForm;
