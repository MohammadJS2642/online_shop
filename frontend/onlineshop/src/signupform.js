import { useEffect } from "react";
import FetchData from "./api/fetchapi";

function SignupForm() {
  useEffect(() => {
    FetchData();
  }, []);
  return (
    <form action="" method="POST">
      <input type="text" />
      <br />
      <input type="text" />
      <br />
      <input type="text" />
      <br />
      <input type="submit" />
    </form>
  );
}

export default SignupForm;
