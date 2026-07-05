import React from "react";
import { Composition } from "remotion";
import { Video } from "./Video";

const storyboard = require("../output/storyboard.json");

export const Root: React.FC = () => {
  return (
    <>
      <Composition
        id="WeddingVideo"
        component={Video}
        durationInFrames={storyboard.total_duration * 30}
        fps={30}
        width={1080}
        height={1920}
      />
    </>
  );
};